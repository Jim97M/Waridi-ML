from typing import Dict, List

MAX_HISTORY_MESSAGES = 20

conversations: Dict[str, List[dict]] = {}


def get_conversation(conversation_id: str) -> List[dict]:
    return conversations.get(conversation_id, [])


def save_conversation(
    conversation_id: str,
    messages: List[dict]
):
    conversations[conversation_id] = messages[-MAX_HISTORY_MESSAGES:]
    