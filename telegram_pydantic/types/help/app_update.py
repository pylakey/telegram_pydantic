from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AppUpdate(BaseModel):
    """
    types.help.AppUpdate
    ID: 0xccbbce30
    Layer: 181
    """
    QUALNAME: typing.Literal['types.help.AppUpdate', 'AppUpdate'] = pydantic.Field(
        'types.help.AppUpdate',
        alias='_'
    )

    id: int
    version: str
    text: str
    entities: list["base.MessageEntity"]
    can_not_skip: typing.Optional[bool] = None
    document: typing.Optional["base.Document"] = None
    url: typing.Optional[str] = None
    sticker: typing.Optional["base.Document"] = None
