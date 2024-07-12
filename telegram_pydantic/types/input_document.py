from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputDocument(BaseModel):
    """
    types.InputDocument
    ID: 0x1abfb575
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputDocument', 'InputDocument'] = pydantic.Field(
        'types.InputDocument',
        alias='_'
    )

    id: int
    access_hash: int
    file_reference: Bytes
