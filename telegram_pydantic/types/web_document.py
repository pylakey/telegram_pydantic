from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class WebDocument(BaseModel):
    """
    types.WebDocument
    ID: 0x1c570ed1
    Layer: 181
    """
    QUALNAME: typing.Literal['types.WebDocument', 'WebDocument'] = pydantic.Field(
        'types.WebDocument',
        alias='_'
    )

    url: str
    access_hash: int
    size: int
    mime_type: str
    attributes: list["base.DocumentAttribute"]
