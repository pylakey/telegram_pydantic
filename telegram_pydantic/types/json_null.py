from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class JsonNull(BaseModel):
    """
    types.JsonNull
    ID: 0x3f6d7b68
    Layer: 181
    """
    QUALNAME: typing.Literal['types.JsonNull', 'JsonNull'] = pydantic.Field(
        'types.JsonNull',
        alias='_'
    )

