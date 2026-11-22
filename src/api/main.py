from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from src.agent.prompts import WARIDI_SYSTEM_PROMPT
from src.agent.conversation import (
    get_conversation,
    save_conversation
)
from src.services.llm_service import generate_response, provider, model


app = FastAPI(
    title="Waridi ML Service",
    description="Conversational AI service for Waridi",
    version="0.1.0"
)


class ChatRequest(BaseModel):
    conversation_id: str = Field(min_length=1)
    message: str = Field(min_length=1, max_length=10000)


class ChatResponse(BaseModel):
    conversation_id: str
    response: str
    provider: str
    model: str


@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "service": "waridi-ml",
        "provider": provider,
        "model": model
    }


@app.post("/api/v1/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):

    try:
        history = get_conversation(request.conversation_id)

        messages = [
            {
                "role": "system",
                "content": WARIDI_SYSTEM_PROMPT
            },
            *history,
            {
                "role": "user",
                "content": request.message
            }
        ]

        assistant_response = await generate_response(messages)

        updated_history = [
            *history,
            {
                "role": "user",
                "content": request.message
            },
            {
                "role": "assistant",
                "content": assistant_response
            }
        ]

        save_conversation(
            request.conversation_id,
            updated_history
        )

        return ChatResponse(
            conversation_id=request.conversation_id,
            response=assistant_response,
            provider=provider,
            model=model
        )

    except Exception as error:
        print(f"Chat service error: {error}")

        raise HTTPException(
            status_code=502,
            detail="Unable to generate a response from the AI provider."
        )
        