from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPrivacyKeyBirthday(BaseModel):
    """
    types.InputPrivacyKeyBirthday
    ID: 0xd65a11cc
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPrivacyKeyBirthday', 'InputPrivacyKeyBirthday'] = pydantic.Field(
        'types.InputPrivacyKeyBirthday',
        alias='_'
    )

