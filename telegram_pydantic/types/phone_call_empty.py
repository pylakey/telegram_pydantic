from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PhoneCallEmpty(BaseModel):
    """
    types.PhoneCallEmpty
    ID: 0x5366c915
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PhoneCallEmpty', 'PhoneCallEmpty'] = pydantic.Field(
        'types.PhoneCallEmpty',
        alias='_'
    )

    id: int
