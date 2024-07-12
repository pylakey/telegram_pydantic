from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMediaEmpty(BaseModel):
    """
    types.InputMediaEmpty
    ID: 0x9664f57f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMediaEmpty', 'InputMediaEmpty'] = pydantic.Field(
        'types.InputMediaEmpty',
        alias='_'
    )

