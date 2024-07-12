from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EditChatTitle(BaseModel):
    """
    functions.messages.EditChatTitle
    ID: 0x73783ffd
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.EditChatTitle', 'EditChatTitle'] = pydantic.Field(
        'functions.messages.EditChatTitle',
        alias='_'
    )

    chat_id: int
    title: str
