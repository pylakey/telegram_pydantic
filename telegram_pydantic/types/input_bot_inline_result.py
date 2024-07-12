from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputBotInlineResult(BaseModel):
    """
    types.InputBotInlineResult
    ID: 0x88bf9319
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputBotInlineResult', 'InputBotInlineResult'] = pydantic.Field(
        'types.InputBotInlineResult',
        alias='_'
    )

    id: str
    type: str
    send_message: "base.InputBotInlineMessage"
    title: typing.Optional[str] = None
    description: typing.Optional[str] = None
    url: typing.Optional[str] = None
    thumb: typing.Optional["base.InputWebDocument"] = None
    content: typing.Optional["base.InputWebDocument"] = None
