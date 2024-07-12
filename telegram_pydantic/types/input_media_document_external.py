from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMediaDocumentExternal(BaseModel):
    """
    types.InputMediaDocumentExternal
    ID: 0xfb52dc99
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMediaDocumentExternal', 'InputMediaDocumentExternal'] = pydantic.Field(
        'types.InputMediaDocumentExternal',
        alias='_'
    )

    url: str
    spoiler: typing.Optional[bool] = None
    ttl_seconds: typing.Optional[int] = None
