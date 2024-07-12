from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BotInlineMessageText(BaseModel):
    """
    types.BotInlineMessageText
    ID: 0x8c7f65e2
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BotInlineMessageText', 'BotInlineMessageText'] = pydantic.Field(
        'types.BotInlineMessageText',
        alias='_'
    )

    message: str
    no_webpage: typing.Optional[bool] = None
    invert_media: typing.Optional[bool] = None
    entities: typing.Optional[list["base.MessageEntity"]] = None
    reply_markup: typing.Optional["base.ReplyMarkup"] = None
