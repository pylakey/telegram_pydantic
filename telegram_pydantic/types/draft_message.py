from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DraftMessage(BaseModel):
    """
    types.DraftMessage
    ID: 0x3fccf7ef
    Layer: 181
    """
    QUALNAME: typing.Literal['types.DraftMessage', 'DraftMessage'] = pydantic.Field(
        'types.DraftMessage',
        alias='_'
    )

    message: str
    date: Datetime
    no_webpage: typing.Optional[bool] = None
    invert_media: typing.Optional[bool] = None
    reply_to: typing.Optional["base.InputReplyTo"] = None
    entities: typing.Optional[list["base.MessageEntity"]] = None
    media: typing.Optional["base.InputMedia"] = None
