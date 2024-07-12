from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecurePasswordKdfAlgoUnknown(BaseModel):
    """
    types.SecurePasswordKdfAlgoUnknown
    ID: 0x4a8537
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecurePasswordKdfAlgoUnknown', 'SecurePasswordKdfAlgoUnknown'] = pydantic.Field(
        'types.SecurePasswordKdfAlgoUnknown',
        alias='_'
    )

