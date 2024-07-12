from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputBotInlineResultDocument(BaseModel):
    """
    types.InputBotInlineResultDocument
    ID: 0xfff8fdc4
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputBotInlineResultDocument', 'InputBotInlineResultDocument'] = pydantic.Field(
        'types.InputBotInlineResultDocument',
        alias='_'
    )

    id: str
    type: str
    document: "base.InputDocument"
    send_message: "base.InputBotInlineMessage"
    title: typing.Optional[str] = None
    description: typing.Optional[str] = None
