from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SentCodeTypeApp(BaseModel):
    """
    types.auth.SentCodeTypeApp
    ID: 0x3dbb5986
    Layer: 181
    """
    QUALNAME: typing.Literal['types.auth.SentCodeTypeApp', 'SentCodeTypeApp'] = pydantic.Field(
        'types.auth.SentCodeTypeApp',
        alias='_'
    )

    length: int
