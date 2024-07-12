from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageMediaDocument(BaseModel):
    """
    types.MessageMediaDocument
    ID: 0x4cf4d72d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageMediaDocument', 'MessageMediaDocument'] = pydantic.Field(
        'types.MessageMediaDocument',
        alias='_'
    )

    nopremium: typing.Optional[bool] = None
    spoiler: typing.Optional[bool] = None
    video: typing.Optional[bool] = None
    round: typing.Optional[bool] = None
    voice: typing.Optional[bool] = None
    document: typing.Optional["base.Document"] = None
    alt_document: typing.Optional["base.Document"] = None
    ttl_seconds: typing.Optional[int] = None
