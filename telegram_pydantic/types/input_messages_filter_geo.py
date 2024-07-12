from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMessagesFilterGeo(BaseModel):
    """
    types.InputMessagesFilterGeo
    ID: 0xe7026d0d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMessagesFilterGeo', 'InputMessagesFilterGeo'] = pydantic.Field(
        'types.InputMessagesFilterGeo',
        alias='_'
    )

