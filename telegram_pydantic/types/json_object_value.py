from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class JsonObjectValue(BaseModel):
    """
    types.JsonObjectValue
    ID: 0xc0de1bd9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.JsonObjectValue', 'JsonObjectValue'] = pydantic.Field(
        'types.JsonObjectValue',
        alias='_'
    )

    key: str
    value: "base.JSONValue"
