
from pydantic import BaseModel, Field, create_model
from typing import List, Type, Any
from enum import Enum
from pydantic.fields import FieldInfo
from pydantic_core import PydanticUndefined

class AttributionItem(BaseModel):
    quoted_statement: str = Field(
        ...,
        description="The direct quote from the speech sample."
    )
    reasoning: str = Field(
        ...,
        description="Explanation of why this quote reflects the given attribution."
    )

class ReviewCategory(str, Enum):
    Stable_Unchangeable = "Stable_Unchangeable"
    Fluctuate_Changeable = "Fluctuate_Changeable"
    Deliberate = "Deliberate"
    Unintentional = "Unintentional"
    Controllable_Regulated = "Controllable_Regulated"
    Uncontrollable_Unregulated = "Uncontrollable_Unregulated"
    Locus_External = "Locus_External"
    Locus_Internal_Bad_Unlikeable = "Locus_Internal_Bad_Unlikeable"
    Locus_Internal_Good_Likeable = "Locus_Internal_Good_Likeable"

class Critique(str, Enum):
    missing = "missing"
    superfluous = "superfluous"

class ReviewItem(BaseModel):
    category: ReviewCategory
    critique: Critique 
    quoted_statement: str = Field(
        ...,
        description="Missing statement that needs to be quoted from 'Test Case Interview Transcript' or superfluous statement that needs to be removed from the 'Attribution Analysis', according to PASS MANUAL(s) and inclusion/exclusion criteria."
    )
    reasoning: str = Field(
        ...,
        description="Support of the critique according to contents of the PASS MANUAL(s) and inclusion/exclusion criteria."
    )

class Permanence(BaseModel):
    Stable_Unchangeable: List[AttributionItem] = Field(
        default_factory=list,
        description="Child's disruptive behaviour was believed to be a long-standing issue that has not seen any improvements over time. This includes beliefs that the child’s behaviour is fixed and unchangeable regardless of whether there were any efforts by parents or other services to encourage positive improvements."
    )
    Fluctuate_Changeable: List[AttributionItem] = Field(
        default_factory=list,
        description="Child's disruptive behaviour was believed to be shiftable over time, amenable to change, or that there is some belief that these behaviours can be improved over time. This can include a temporal reference to the child’s behaviour."
    )

class Intentionality(BaseModel):
    Deliberate: List[AttributionItem] = Field(
        default_factory=list,
        description="Child’s disruptive behaviour was believed to be deliberate, intentional or planned. This entails a belief that the child has some form of cognitive capacity to engage in goal-directed antisocial behaviours to achieve something that they want to happen."
    )
    Unintentional: List[AttributionItem] = Field(
        default_factory=list,
        description="Child’s disruptive behaviour was believed to be unintentional or unplanned. This includes an element of ignorance or unawareness that the child has towards their own behaviour."
    )

class Controllability(BaseModel):
    Controllable_Regulated: List[AttributionItem] = Field(
        default_factory=list,
        description="Child’s disruptive behaviour was believed to be within their control. This is perceived to be a desirable behaviour whereby the child possesses the ability for self-regulation of their disruptive behaviours."
    )
    Uncontrollable_Unregulated: List[AttributionItem] = Field(
        default_factory=list,
        description="Child’s disruptive behaviour was believed to be out of their control. This is perceived to be an undesirable behaviour whereby the child lacks the ability for self-regulation of their disruptive behaviour."
    )

class LocusOfControl(BaseModel):
    Locus_External: List[AttributionItem] = Field(
        default_factory=list,
        description="Child's disruptive behaviour was attributed to external factors around the child, such as school, peer influence, family influence or a disorder/diagnosis. This can include perceptions about whether the child is able to be managed or controlled by parental or professional efforts."
    )
    Locus_Internal_Bad_Unlikeable: List[AttributionItem] = Field(
        default_factory=list,
        description="Child’s disruptive behaviour was attributed to undesirable traits and qualities that suggest unlikability or badness."
    )
    Locus_Internal_Good_Likeable: List[AttributionItem] = Field(
        default_factory=list,
        description="Child’s disruptive behaviour was attributed to desirable traits and qualities that suggest likeability or goodness."
    )

class ReviewResponse(BaseModel):
    reviews: List[ReviewItem] = Field(
        default_factory=list,
        description="List of reviews for the attributions, including category, review statement, and reasoning. Only include reviews that are necessary to correct misclassifications or errors based on the manual and inclusion/exclusion criteria."
    )

class AttributionResponse(BaseModel):
    PERMANENCE: Permanence = Field(
        ...,
        description="Attributions about the stability or changeability of the child’s behavioural/emotional problems. Refer to Adapted PASS MANUAL TO IDENTIFY PERMANENCE ATTRIBUTION."
    )
    INTENTIONALITY: Intentionality = Field(
        ...,
        description="Attributions about whether the child’s behaviour is seen as deliberate or unintentional. Refer to Adapted PASS MANUAL TO IDENTIFY INTENTIONALITY ATTRIBUTION."
    )
    CONTROLLABILITY: Controllability = Field(
        ...,
        description="Attributions about whether the child’s behaviour is perceived as controllable or not. Refer to Adapted PASS MANUAL TO IDENTIFY CONTROLLABILITY ATTRIBUTION."
    )
    LOCUS_OF_CONTROL: LocusOfControl = Field(
        ...,
        description="Attributions about whether the cause of behaviour is internal or external to the child, and whether internal causes are seen as good or bad. Refer to Adapted PASS MANUAL TO IDENTIFY LOCUS-OF-CONTROL ATTRIBUTION."
    )

def reduce_model_to_field(model_cls: Type[BaseModel], field_name: str) -> Type[BaseModel]:
    """
    Create a new Pydantic model with only the specified field from the original model.
    Args:
        model_cls: The original Pydantic model class.
        field_name: The name of the field to retain in the new model.
    Returns:
        A new Pydantic model class with only the specified field.
    Raises:
        ValueError: If the field_name is not present in the model_cls.
    """
    if field_name not in model_cls.model_fields:
        raise ValueError(f"{field_name} is not a valid field in {model_cls.__name__}")

    field = model_cls.model_fields[field_name]  # ← this is a FieldInfo in Pydantic v2
    field_type = field.annotation
    field_info: FieldInfo = field

    # Required if default is not set
    default: Any = field.default if field.default is not PydanticUndefined else ...

    # Recreate the new model with one field
    NewModel = create_model(
        model_cls.__name__,
        **{field_name: (field_type, Field(default, **(field_info.json_schema_extra or {})))}
    )

    return NewModel
