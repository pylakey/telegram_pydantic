from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DocumentAttributeImageSize(BaseModel):
    """
    types.DocumentAttributeImageSize
    ID: 0x6c37c15c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.DocumentAttributeImageSize', 'DocumentAttributeImageSize'] = pydantic.Field(
        'types.DocumentAttributeImageSize',
        alias='_'
    )

    w: int
    h: int
