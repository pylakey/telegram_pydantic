from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BotInlineMessageMediaWebPage(BaseModel):
    """
    types.BotInlineMessageMediaWebPage
    ID: 0x809ad9a6
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BotInlineMessageMediaWebPage', 'BotInlineMessageMediaWebPage'] = pydantic.Field(
        'types.BotInlineMessageMediaWebPage',
        alias='_'
    )

    message: str
    url: str
    invert_media: typing.Optional[bool] = None
    force_large_media: typing.Optional[bool] = None
    force_small_media: typing.Optional[bool] = None
    manual: typing.Optional[bool] = None
    safe: typing.Optional[bool] = None
    entities: typing.Optional[list["base.MessageEntity"]] = None
    reply_markup: typing.Optional["base.ReplyMarkup"] = None
