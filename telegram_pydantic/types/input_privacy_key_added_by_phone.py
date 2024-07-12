from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPrivacyKeyAddedByPhone(BaseModel):
    """
    types.InputPrivacyKeyAddedByPhone
    ID: 0xd1219bdd
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPrivacyKeyAddedByPhone', 'InputPrivacyKeyAddedByPhone'] = pydantic.Field(
        'types.InputPrivacyKeyAddedByPhone',
        alias='_'
    )

