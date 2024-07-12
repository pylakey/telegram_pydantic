from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BotInlineResult(BaseModel):
    """
    types.BotInlineResult
    ID: 0x11965f3a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BotInlineResult', 'BotInlineResult'] = pydantic.Field(
        'types.BotInlineResult',
        alias='_'
    )

    id: str
    type: str
    send_message: "base.BotInlineMessage"
    title: typing.Optional[str] = None
    description: typing.Optional[str] = None
    url: typing.Optional[str] = None
    thumb: typing.Optional["base.WebDocument"] = None
    content: typing.Optional["base.WebDocument"] = None
