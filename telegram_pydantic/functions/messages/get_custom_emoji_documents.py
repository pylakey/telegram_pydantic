from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetCustomEmojiDocuments(BaseModel):
    """
    functions.messages.GetCustomEmojiDocuments
    ID: 0xd9ab0f54
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetCustomEmojiDocuments', 'GetCustomEmojiDocuments'] = pydantic.Field(
        'functions.messages.GetCustomEmojiDocuments',
        alias='_'
    )

    document_id: list[int]
