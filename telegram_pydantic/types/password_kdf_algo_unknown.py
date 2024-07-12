from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PasswordKdfAlgoUnknown(BaseModel):
    """
    types.PasswordKdfAlgoUnknown
    ID: 0xd45ab096
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PasswordKdfAlgoUnknown', 'PasswordKdfAlgoUnknown'] = pydantic.Field(
        'types.PasswordKdfAlgoUnknown',
        alias='_'
    )

