from dotenv import load_dotenv
from openai import OpenAI
import os
import json

load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

api_key = os.getenv('OPENAI_API_KEY')
if api_key:
    # Set it explicitly for the OpenAI client
    os.environ['OPENAI_API_KEY'] = api_key
else:
    print('Warning: OPENAI_API_KEY not found in .env file')
