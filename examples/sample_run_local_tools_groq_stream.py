"""Groq Sample"""
import os
from typing import List
from dotenv import load_dotenv
from groq import Groq
from toolhouse import Toolhouse
from toolhouse.models.OpenAIStream import OpenAIStream

load_dotenv()

TOKEN = os.getenv("GROQCLOUD_API_KEY")
TH_TOKEN = os.getenv("TOOLHOUSE_BEARER_TOKEN")

client = Groq(api_key=TOKEN)

local_tools = [
    {'type': 'function',
     'function':
         {
             'name': 'hello',
             'description': 'The user receives a customized hello message from a city and returns it to the user.', 
             'parameters': {
                 'type': 'object',
                 'properties': {
                     'city': {'type': 'string', 'description': 'The city where you are from'}
                 }},
             'required': ['city']
         }}]

th = Toolhouse(access_token=TH_TOKEN, provider="openai")
th.set_metadata("id", "fabio")
th.set_metadata("timezone", 5)


@th.register_local_tool("hello")
def hello_tool(city: str):
    """Return a Hello message from a specific city."""
    return f"Hello from {city}!!!"


messages: List = [{
    "role": "user",
    "content":
        "Can I get a hello from Rome?"
    }]


stream = client.chat.completions.create(
    model='gpt-4o',
    messages=messages,
    tools=th.get_tools() + local_tools,
    stream=True
)

# Use the stream and save blocks
stream_storage = OpenAIStream()
for block in stream:  # pylint: disable=E1133
    print(block)
    stream_storage.add(block)

messages += th.run_tools(stream_storage, stream=True)

response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            tools=th.get_tools() + local_tools
        )
print(response.choices[0].message.content)