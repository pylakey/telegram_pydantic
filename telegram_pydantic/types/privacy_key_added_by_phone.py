from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PrivacyKeyAddedByPhone(BaseModel):
    """
    types.PrivacyKeyAddedByPhone
    ID: 0x42ffd42b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PrivacyKeyAddedByPhone', 'PrivacyKeyAddedByPhone'] = pydantic.Field(
        'types.PrivacyKeyAddedByPhone',
        alias='_'
    )

