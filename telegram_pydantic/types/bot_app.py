from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BotApp(BaseModel):
    """
    types.BotApp
    ID: 0x95fcd1d6
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BotApp', 'BotApp'] = pydantic.Field(
        'types.BotApp',
        alias='_'
    )

    id: int
    access_hash: int
    short_name: str
    title: str
    description: str
    photo: "base.Photo"
    hash: int
    document: typing.Optional["base.Document"] = None
