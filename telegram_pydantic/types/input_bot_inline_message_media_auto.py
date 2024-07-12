from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputBotInlineMessageMediaAuto(BaseModel):
    """
    types.InputBotInlineMessageMediaAuto
    ID: 0x3380c786
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputBotInlineMessageMediaAuto', 'InputBotInlineMessageMediaAuto'] = pydantic.Field(
        'types.InputBotInlineMessageMediaAuto',
        alias='_'
    )

    message: str
    invert_media: typing.Optional[bool] = None
    entities: typing.Optional[list["base.MessageEntity"]] = None
    reply_markup: typing.Optional["base.ReplyMarkup"] = None
