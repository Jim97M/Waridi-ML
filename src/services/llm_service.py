import os
from dotenv import load_dotenv
from openai import AsyncOpenAI

load_dotenv()

provider = os.getenv("LLM_PROVIDER", "openai").lower()
api_key = os.getenv("LLM_API_KEY")
model = os.getenv("LLM_MODEL")
base_url = os.getenv("LLM_BASE_URL")

if not api_key:
    raise ValueError("LLM_API_KEY is missing from .env")

if not model:
    raise ValueError("LLM_MODEL is missing from .env")

client_options = {
    "api_key": api_key,
}

if base_url:
    client_options["base_url"] = base_url

client = AsyncOpenAI(**client_options)


async def generate_response(messages: list) -> str:

    response = await client.chat.completions.create(
        model=model,
        messages=messages,
    )

    content = response.choices[0].message.content

    if not content:
        raise RuntimeError("The LLM returned an empty response")

    return content

