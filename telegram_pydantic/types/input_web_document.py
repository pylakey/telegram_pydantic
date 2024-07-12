from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputWebDocument(BaseModel):
    """
    types.InputWebDocument
    ID: 0x9bed434d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputWebDocument', 'InputWebDocument'] = pydantic.Field(
        'types.InputWebDocument',
        alias='_'
    )

    url: str
    size: int
    mime_type: str
    attributes: list["base.DocumentAttribute"]
