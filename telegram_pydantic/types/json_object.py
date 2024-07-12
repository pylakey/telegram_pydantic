from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class JsonObject(BaseModel):
    """
    types.JsonObject
    ID: 0x99c1d49d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.JsonObject', 'JsonObject'] = pydantic.Field(
        'types.JsonObject',
        alias='_'
    )

    value: list["base.JSONObjectValue"]
