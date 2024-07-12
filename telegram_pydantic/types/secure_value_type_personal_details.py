from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecureValueTypePersonalDetails(BaseModel):
    """
    types.SecureValueTypePersonalDetails
    ID: 0x9d2a81e3
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecureValueTypePersonalDetails', 'SecureValueTypePersonalDetails'] = pydantic.Field(
        'types.SecureValueTypePersonalDetails',
        alias='_'
    )

