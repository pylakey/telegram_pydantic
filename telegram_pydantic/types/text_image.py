from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TextImage(BaseModel):
    """
    types.TextImage
    ID: 0x81ccf4f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.TextImage', 'TextImage'] = pydantic.Field(
        'types.TextImage',
        alias='_'
    )

    document_id: int
    w: int
    h: int
