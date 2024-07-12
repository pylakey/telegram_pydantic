from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PhotoStrippedSize(BaseModel):
    """
    types.PhotoStrippedSize
    ID: 0xe0b0bc2e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PhotoStrippedSize', 'PhotoStrippedSize'] = pydantic.Field(
        'types.PhotoStrippedSize',
        alias='_'
    )

    type: str
    bytes: Bytes
