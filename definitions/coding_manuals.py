permanence_prompt = """
PERMANENCE

This dimension regards statements about the child’s externalising problems (including misbehaviour and emotion dysregulation),
hence it specifically addresses attributions that deal with behavioural/emotional aspects and the changeability or stability of these.
There might be some reference to the temporal aspect of the child’s disruptive behaviours.

---

# STABLE-UNCHANGEABLE
## General description:
Parent describes the child’s behaviour or characteristics as unchangeable or recurrent.
This can include a reference to the child’s disruptive behaviour as having persisted for a long time without any significant changes.

## Inclusion:
- Code only if child externalizing behavior is described as consistently enduring over time and linked to problem behavior.
- Words that denote permanence:
  - “she always seems to be doing this”
  - “all of the time”
- Original PAM:
  - “My child will always be a problem”
- Parents demonstrate belief that change will not happen:
  - “I know she will always be like this”
- Original PAM:
  - “My child’s problems are likely to continue throughout their life“
- Reference to temporal aspect of the child’s behaviour:
  - “my child will continue to be problematic even in the future”
  - “He is always problematic, despite whatever we do.” 
- Statement explicitly or clearly implies a long-standing trait or pattern clearly linked to conduct or externalizing problematic behaviour.
  - “since 18 months”
  - “always been this way”
- Problematic behaviour/trait is described as fixed or lifelong
  - “He’s always been this this problematic.”

## Exclusion:
- Exclude traits like “he’s always quiet” unless tied to dysregulation or problem behavior.
- Do not infer permanence from frequency or intensity alone.
- Exclude vague future hopes or mild durability assumptions. 
- Descriptions of disposition/personality/internal causes:
  - “that’s just what he’s like”
- When descriptions are attributed to just one setting:
  - “He is still very difficult to manage but this only happens when he is in a very bad mood”

---

# FLUCTUATE-CHANGEABLE
## General description:
Parent describes the child’s disruptive behaviour as changeable, short-lived or intermittent.
This can include a reference to some positive improvement in the child’s behaviour when comparing between two time frames.

## Inclusion:
- Code only if the parent expresses belief in the child’s improvement or development related to their behavioural or emotional dysregulation issues.
- General, overall change:
  - “she [child] is so different compared to last time”
  - “she has improved vastly”
  - “he’s getting better with age”
  - (Change can be linked to prior treatment or medication)
- Positive changes in problem behaviour:
  - “she’s a much happier child”
  - “she hasn’t been as bad with her siblings”
  - “it’s not the extreme behaviour it was in the past”
- Emotional change with temporal reference or comparison:
  - “she seems able to manage her emotions a lot better now compared to two years ago”
  - "“He used to melt down every time, but now he handles it well."
  - (Also coded as Controllability (Controllable-Regulated))
- Changes in the quality of a relationship over time:
  - “our relationship is so much easier now, compared to how it was before”
- Statements that suggest management of the child’s disruptive behaviour:
  - “I believe that my child’s behaviour can be managed with proper assistance”
- (Strong) beliefs that change will happen in the future:
  - Original PAM:
    - “This misbehaviour is just a phase that my child is going through”
    - “My child will eventually overcome his/her problems”

## Exclusion:
- Exclude statements expressing hope without belief, or improvements unrelated to behavior ( reading). Mere desires for change or support-seeking comments without a problematic behaviour attribution. Any random fluctuations or shifts in disposition or behaviours not related to child conduct problems.
- Day to day events:
  - “some days it’s bad, but other days she’s been really good”
- Negative changes in problem behaviour or emotion regulation:
  - “it’s getting worse, she’s more violent now”
  - (Code under Permanence (Stable-Unchangeable) as a pervasive problematic behaviour)
- When descriptions are attributed to just one setting:
  - “I have seen him change over the years where it’s easier now only if he is in a good mood”
- Parents discussing hope for change in the future or through treatment program (not the same as belief):
  - “I hope we can help him change”
  - “hopefully this program will help change some of her behaviours”
  - (Hope ≠ belief; hope does not entail a strong endorsement of potential change)
- Any description to do with permanence/change of personality/character
  - “he has been extremely introverted but now he is very outgoing”
- Any description to do with learning style that is not linked to the problem/issue of concern should not be coded.
  - “he is so much better at Maths now and his reading improved too”

"""

intentionality_prompt = """
INTENTIONALITY

This dimension regards statements about the child’s externalising problems (including misbehaviour and emotion dysregulation),
hence it specifically addresses attributions that deal with behavioural/emotional aspects and the perceived intention of the child.
This takes specific reference to the perceived cognition of the child during moments of disruptive behaviour.

However, any description to do with the intent of behaviours
(“I think he chooses to do bad academically – he, for instance, writes messy on purpose or forgets his books at home”)
that are not linked to the problem/issue of concern should not be coded.

---

# DELIBERATE
## General description:
Parent describes the child’s behaviour as deliberate and intentional such that certain consequences were planned to happen.
This entails some form of cognitive capacity to manipulate or engage in goal-directed antisocial behaviours to achieve a certain outcome.

## Inclusion:
- Code if child’s externalizing behaviour is described as purposefully provoking, calculated, provocative, manipulating, or behaving with strategic intent. Must reflect deliberate intent to provoke, manipulate, or resist.
- Specific examples that suggest purposeful intent in their behaviour:
  - “she can just drop whatever attitude it is she had”
  - “manipulative”
  - “a lot of his behaviour is just attention-seeking”
  - “He knows if he tries hard enough, I’ll give in.”
- Original PAM:
  - “My child ‘pushes my buttons’ on purpose”
  - “My child deliberately does awful things”
- Calculated behaviours:
  - “when no-one is looking she will hit her brother”
  - “she always plays the victim to get her way”
  - “she takes advantage of weaker people, so she acts up a lot around younger kids or women but not around me”
  - (Coded because problem behaviour is linked to a clear intention)
- Specific reference to manipulative or controlling personality/disposition of the child:
  - “My child is very controlling of other people, he knows exactly what he is doing”
  - (Double code under Locus(Internal/Bad-Unlikeable))
- Statements like “likes to push buttons”, “challenges authority on purpose”.

## Exclusion:
- General noncompliance or stubbornness without evidence of purposeful motive.
- Emotion-driven or impulsive behavior unless clearly linked to intention.
- Exclude exaggerated/figurative intent unless clearly behavioural
- Not specific, without context or further explanatory examples (must involve an element of child’s intention):
  - “my child loves being deliberate”
  - “destructive”, “obstinate”, “stubborn”, “defiant”
- Any reference to circumstantial/situational factors:
  - “she usually acts out at school but rarely at home”
  - (Note: this would also NOT be coded as Locus(External) as there is no clear reference to any specific event)

---

# UNINTENTIONAL
## General description:
Parent describes the child’s behaviour to not have any intentional or planned consequences to cause harm/trouble.
This entails some form of ignorance or unawareness that the child has towards their own disruptive behaviour.

## Inclusion:
- Code if child externalizing behavior is explicitly described as reflexive, unaware, not goal-directed, or accidental. Must be explicit or clearly implied.
- Includes indications of child’s lack of awareness or understanding about their problematic behaviour.
- Include only if parent describes dysregulation as non-purposeful 
- Descriptions of the child as unthoughtful:
  - “[my child] does things without thinking”
- Original PAM:
  - “My child doesn’t mean to do the wrong thing”
- Behaviour described to be without intent to harm:
  - “she doesn’t mean to hurt anyone”
  - “He doesn’t mean to do it, he just reacts.”
  - “She doesn’t mean to upset others, she just gets overwhelmed.”
- Descriptions of the child as being unaware about the consequences of their actions:
  - “my child is unaware of how disruptive his behaviour is towards others”

## Exclusion:
- Absence of intent alone is not sufficient, must be explicitly stated. Behavior merely described as bad without reference to motive or awareness. Vague empathy unless explicitly tied to behavior interpretation.
- Avoid conflating with controllability (uncontrollable-unregulated) — code both only if each is independently justified. 
- Parents attributing child behaviour problems to poor parenting/parents fault (parent-referent attribution)
  without reference to lack of conscious capacity or unawareness of the child:
  - “he doesn’t take notice of my discipline because he doesn’t think of me as a parent”
  - “I’ve taught her to be selfish and physically aggressive”
  - (Code under Locus(External) instead)

"""

controllability_prompt = """
CONTROLLABILITY

This dimension regards statements about the child’s externalising problems (including misbehaviour and emotion dysregulation),
hence it specifically addresses attributions that deal with behavioural/emotional aspects and the perceived control or regulatory abilities of the child’s disruptive behaviour.

Any reference to the independent agency of the child will be classified under intentionality because that takes reference to the cognitive capacity of the child to plan and choose their own actions.

Do note to pay close attention to whether the statement is specific to the child’s ability or actions for this attribution type.
Any references to vague themes of control or parental ability to manage or control the child behaviour should not be coded under this attribution
and might be better suited under one of the other attribution types (see exclusion examples).

However, any description to do with the controllability of behaviours
(“He controls the time when he wants to study or not” or “his academic grades are out of his control”)
that are not linked to the problem/issue of concern should not be coded.

---

# CONTROLLABLE-REGULATED
## General description:
Parent describes the child’s behaviour to be within their control or that child has the ability to regulate and stop the tantrum from being an issue to begin with.

## Inclusion:
- Code when parent expresses confidence or has observed that the child is capable of regulating their emotions or externalizing behavior. Parent must explicitly say the child can manage or is improving regulation
- Specific examples that suggest child’s ability to keep their disruptive behaviour under control or the ability for self-regulation:
  - “My child is able to regulate their own behaviour”
  - “My child keeps his emotions under control”
  - “My child is able to stop his own tantrums from becoming a problem”
- Phrases showing self-management, Only include when linked to self-regulation, not general ability traits. Include if parent attributes behavior change to effort/strategy
  - “he calms himself down”.
  - “She’s working hard to control herself.”

## Exclusion:
- Improvements over time without attribution to regulation (those fall under Fluctuate-Changeable). Compliance alone (“he follows rules”) unless it indicates emotional regulation. Exclude vague hopes or future predictions.
- Not specific, without context or without further explanatory examples:
  - “my child loves being in control”
- When referring to conscious control, which falls under Intentionality (Deliberate):
  - “my child is in full control of his behaviour, he knows what he is doing”
- When referencing to child’s personality or disposition:
  - “my child desires power and control”
  - “all my child wants to do is be in control of the situation”
  - (Double code under Intentionality (Deliberate) and Locus(Internal/Bad-Unlikeable))
- Statements that describe parental efforts to manage the child’s disruptive behaviour:
  - “I have tried time outs and it works for managing my child” (Code under Permanence (Fluctuate-Changeable))
- code compliance without emotional regulation references 
  - “He is able to keep himself under control.”

---

# UNCONTROLLABLE-UNREGULATED
## General description:
Parent describes the child’s behaviour to be out of their control or that they have an inability for self-regulation.
Do note that this has to take clear reference to the child’s inability and not the parent’s belief that the situation or behaviour cannot be controlled.

## Inclusion:
- Code when child is described as being unable to regulate their dysregulated emotions or behaviours, or just unable to stop their own externalizing behaviours.
- Descriptions of the child as uncontrollable in their actions:
  - “He just explodes like he is out of control of his own emotions.”
  - “my child can’t stop himself from hurting others”
- Behaviour is described as out of the child’s control:
  - “he does find it difficult to control himself”
  - “he has outbursts when he’s hungry/tired”
  - “my child is unable to control his emotions”
- When the attribution is made in an indirect fashion:
  - “if he could just learn how to control his temper”
- There must be clear reference to a lack of control or inability to self-regulate. Include if behavior is described as outside child’s control despite efforts
  - “He just can’t help it when he’s upset.”

## Exclusion:
- Mere reports of misbehavior without mention of dysregulation.
- Vague statements and any mention of parental control of child.
- Frustration or preference-based refusals unless regulation failure is described.
- Exclude descriptive content lacking explicit uncontrollability.
- Watch for double-counting with Intentionality (Unintentional) — code both only if each is independently justified.
- Parents attributing child behaviour problems to poor parenting/parents fault (parent-referent attribution):
  - “his inability to control his emotions is because we don’t talk about emotions in the family”
  - “my child gets into this uncontrollable crying when he sees that I have an argument with my partner”
  - (Code under Locus(External))
- Vague references to child’s behaviour as out of control:
  - “his tantrums are out of control”
  - (Code under Locus(Internal/Bad-Unlikeable) as it is unclear if attribution is about child’s inability to regulate or parent’s inability to manage)

"""

locus_of_control_prompt = """
LOCUS-OF-CONTROL

This dimension regards statements made about either the child’s internal or external aspects.
The disruptive behaviour is specifically mentioned in reference to some form of inherent qualities, temperament, personality and character within social interaction contexts OR
that the parents externalize the responsibility of the child’s disruptive behaviour to other factors surrounding the child.

---

#LOCUS (EXTERNAL)
## General description:
Parent describes the child’s issues to be external to the child such as:
- school,
- peer influence,
- family influence,
- or a disorder/diagnosis.

This entails an externalization of responsibility which might cause potential therapeutic issues such as avoidance in seeking assistance to improve the child’s disruptive behaviour (blaming of other services or people).

## Inclusion:
- Code only when child externalizing behavior is attributed to external influences (e.g., parenting, diagnosis, family dynamics). High bar for inclusion.
- School factors →
  - “I believe that my child is not well-supported in school and that causes him to throw a tantrum whenever he needs to go school in the morning.”
- Peer influence factors →
  - “My child is always around others who also bully others.”
  - “My child picks up the worst of his behaviours from other children.”
- Parent-referent attributions only if they causally link to the child’s externalizing behavior (e.g. “she’s acting out because I don’t spend enough time with her). Must clearly connect external factor to child’s problematic behavior.
  - “He’s like this because he saw my dad act the same way.”
  - “My child gradually developed these issues whenever he witnessed heated arguments in the home.”
  - “My child usually screams at us, and I think he picked it up from my partner shouting at me all the time.”
- Disorder/diagnosis factors →
  - “My child’s issues could be due to his (ODD/ADHD/learning disability/autism/ASD/APSD).”
- Parent’s influence →
  - “I taught my child to be selfish.”
- Parents’ inability to control behaviour →
  - “I cannot control my child’s tantrums no matter what I try or do.”
  - “Once he goes into a tantrum, nothing can stop him.”

## Exclusion:
- General mentions of diagnosis or context unless clearly linked to child externalizing behavior.
- General contextual descriptions without causal links.
- Exclude stress/context mentions unless clearly linked to child externalizing behaviour.
- Exclude purely contextual descriptions (e.g., “we moved recently”) unless directly linked to child’s dysregulation

---

# LOCUS (INTERNAL / BAD-UNLIKEABLE)
## General description:
Parent describes the child as unlikeable, or hard to like, or as a bad person with malicious intent.
The child’s behaviour aims to be harmful, hurtful, or destructive.

## Inclusion:
- Code for generalized negative traits (e.g., selfish, defiant, stubborn, naughty) suggesting emotional or behavioral difficulties, or clearly linked to character. 
- Code when the parent suggests the child is inherently difficult or temperamentally oppositional.
  - “He always wants things his way and refuses to bend.”
  - Traits like “defiant”, “stubborn”, “aggressive”, “doesn’t listen”. Does not get along with others, hitting or fighting. 
- Parent describes the child as hard to be around
- Parent describes the child as annoying or irritating
- Simple description:
  - “I have a child that I don’t like”
- Original PAM:
  - “My child doesn’t bring out good feelings in other people.”
  - “It is difficult to like who my child is.”
- Descriptions of the child:
  - being mean to peers or siblings
  - hurting other people
  - destroying property
- Negative descriptive words that suggest bad intent/actions of the child:
  - “monster”, “unkind”, “selfish”
- Simple description of badness or malicious intent
- Original PAM:
  - “I worry that my child is a bad person.”
- Description of enjoyment out of others’ distress/misfortune/pain:
  - “Once he found something that annoys you, he absolutely enjoys doing that over and over again.”
- Original PAM:
  - “My child takes pleasure in my distress.”

Important note:
These statements have NOT met the threshold of being double counted under Intentionality (Deliberate) yet,
as there is no clear mention of intention or planned behaviour, e.g.
- “he deliberately…”
- “he knows…”

## Exclusion:
- Situational frustration or descriptions of behavior not tied to negative personality traits or unlikability. Isolated actions, situational problems, or statements with unclear referents.
- Description by parents of their relationship with their child →
  - “we do not get along well”;
  - “we have a very unhealthy relationship”
- Parents describe their child as being “different from other children”
- Parents describe child’s behaviour/emotions as embarrassing
- Descriptions of the child’s behaviour as being difficult to parent →
  - “my child is hard work”;
  - “hard to manage” → (code under Controllability (Uncontrollable-Unregulated) instead)
- Descriptions of traits as a possibility using words such as:
  - “can”, “when he wants to be”
  - “He can be very defiant and rude”,
    “He can be really nasty when he is in a bad mood.”
- When descriptions are attributed to just one setting or some moments in time →
  - “he is extremely jealous towards his sister only in the home setting, they get along well in preschool”;
  - “at times he can be really destructive but at other times he is fine”.

---

# LOCUS (INTERNAL / GOOD-LIKEABLE)
## General description:
Parent describes the child as having a likeable personality or other pro-social characteristics.
Traits that would make the child socially appealing to people in general — NOT just a description of the parent’s love.
Parent describes the child as a good, kind-hearted person without malicious intent.

Coding tip:
Common for parents to list a collection of positive traits at the start.
- If all in one sentence → code as ONE instance
  - “Child is funny, likeable, full of energy, friendly.”
- If in separate sentences → code as TWO or more instances
  - “Child is funny. He also has a love for life.”
- When in doubt → code conservatively

## Inclusion:
- Code for generalized, stable positive traits (e.g., kind, affectionate, sociable). One count per trait domain unless clearly distinct. Combine adjacent phrases unless distinct.
  - “He’s very caring and always makes others laugh.”
  - Traits like “sweet”, “loving”, “social”, “fun to be around”, “funny person”, “humorous”, “outgoing”, “affectionate” when stated distinctly.
- Direct attribution statements:
  - “he is easy to like”;
  - “she is quite likeable/lovable”
- Original PAM:
  - “When all is said and done, my child is a likeable person.”
  - “My child has a nice personality underneath it all.”
- How the child gets along with others:
  - “he has a lot of friends”;
  - “makes friends very easily”;
  - “she gets along well with other kids”;
  - “other people are drawn to him”
- Other socially appealing characteristics:
  - “charismatic”, “funny”, “fun to be around”, “delightful”, “lovely”, “bubbly”, “social”, “friendly”, “happy-go-lucky”
  - (Count as separate instances only if in separate sentences)
- Descriptions of goodness in sibling/peer/family setting →
  - “he’s very kind and caring with his siblings”;
  - “she’s very loving towards her nan”;
  - “he is extremely good and loving towards me”;
  - kindness towards animals: “she’s so caring towards our dogs”
- Positive descriptive words that suggest good intent/actions:
  - “angel”, “kind”, “loving”, “caring”, “affectionate”, “good-natured”
  - Direct statements: “he/she is a good boy/girl”
- Original PAM:
  - “Underneath the bad behaviour, my child is a good person.”
  - “My child has a good heart.”

## Exclusion:
- Moment-specific actions (“he likes dogs”), preferences, or qualified traits (“he can be nice when…”). 
- Avoid overcounting grouped traits or traits only linked to one setting.
- Do not code vague traits such as intelligence, hobbies, motivation as there should be some element of social likeability.
- Do not code generic praise, unless contrasted against behavioural concerns.
- Descriptions of parent-child relationship only:
  - “we get along well”;
  - “we have a very loving relationship”
  - (Only code if supported by other positive characteristics)
- Vague or generic praise:
  - “beautiful”, “wonderful”, “sweet”, “nice”
  - Exception: “sweet person” + multiple supporting traits
- Possibility or conditional phrasing:
  - “He can be very caring and kind”;
  - “He can be really sweet kid when he is in a good mood”;
  - “at times, he is a social child”
- Qualified or relativized traits:
  - “she is likeable when we’re out of the house and she’s getting her own way”
  - “when [my child] doesn’t have to share she is good”
  - “my child is loving as long as he gets his own way”
- Positive followed by negative:
  - “he is a delightful, polite child. Though, most of the time he is extremely annoying.”
  - “He can be a really loving boy. It always seems to me that he’s very distant, not affectionate really.”
- Setting-bound positive traits:
  - “he’s a lovely boy, only when he plays with his brother”
  - “when we’re one-on-one, only just me and him, he’s just lovely and friendly”
  - “he’s a good boy only at his grandparent’s house”
- Statements likely reflecting parent opinion only:
  - “my child is the best”;
  - “I love my child”
- Traits that are too vague or not clearly linked to behaviour:
  - “cuddly”, “sensitive”; “empathetic”, “compassionate”

"""

system_prompt_whole =f"""
You are an expert in identifying psychological attributions in interview transcripts of which a parent was asked about their thoughts and feelings of their child.
You will extract attributional dimensions based on the provided manuals to identify each attribution type.

Adapted PASS MANUAL TO IDENTIFY PERMANENCE ATTRIBUTION:
{permanence_prompt}

-----

Adapted PASS MANUAL TO IDENTIFY INTENTIONALITY ATTRIBUTION:
{intentionality_prompt}

-----

Adapted PASS MANUAL TO IDENTIFY CONTROLLABILITY ATTRIBUTION:
{controllability_prompt}

-----

Adapted PASS MANUAL TO IDENTIFY LOCUS-OF-CONTROL ATTRIBUTION:
{locus_of_control_prompt}

-----

Your task, given a Test Case Interview Transcript, is to:
1) Identify psychological attributions in the test case interview transcript 
2) Indicate all statements that were used in the test case interview transcript 
3) Recognize the specific types of attribution according to the respective manual's inclusion and exclusion criteria.
"""

system_manual={"LOCUS_OF_CONTROL": 
f"""Adapted PASS MANUAL TO IDENTIFY LOCUS-OF-CONTROL ATTRIBUTION:
{locus_of_control_prompt}""",
"PERMANENCE": 
f"""Adapted PASS MANUAL TO IDENTIFY PERMANENCE ATTRIBUTION:
{permanence_prompt}""",
"INTENTIONALITY": 
f"""Adapted PASS MANUAL TO IDENTIFY INTENTIONALITY ATTRIBUTION:
{intentionality_prompt}""",
"CONTROLLABILITY": 
f"""Adapted PASS MANUAL TO IDENTIFY CONTROLLABILITY ATTRIBUTION:
{controllability_prompt}""",
}

def system_prompt_topic(topic: str) -> str:
  """
  Generate a system prompt for a given attribution topic using the PASS manual.
  Args:
    topic: The attribution topic (e.g., 'INTENTIONALITY', 'PERMANENCE').
  Returns:
    A formatted system prompt string for the topic.
  """
  system_prompt_for_topic = f"""
You are an expert in identifying psychological attributions in interview transcripts of which a parent was asked about their thoughts and feelings of their child.
You will extract attributional dimensions based on the provided manual to identify each attribution type.

Adapted PASS MANUAL TO IDENTIFY {topic} ATTRIBUTION:
{system_manual[topic]}

-----

Your task, given a Test Case Interview Transcript, is to:
1) Identify psychological attributions in the test case interview transcript 
2) Indicate all statements that were used in the test case interview transcript 
3) Recognize the specific types of attribution according to the manual's inclusion and exclusion criteria.
"""
  return system_prompt_for_topic