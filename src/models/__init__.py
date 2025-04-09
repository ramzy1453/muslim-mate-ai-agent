from agno.models.openai import OpenAIChat
from dotenv import load_dotenv

load_dotenv()

GPT_4O = OpenAIChat(id="gpt-4o")