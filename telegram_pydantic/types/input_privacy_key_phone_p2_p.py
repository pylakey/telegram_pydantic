from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPrivacyKeyPhoneP2P(BaseModel):
    """
    types.InputPrivacyKeyPhoneP2P
    ID: 0xdb9e70d2
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPrivacyKeyPhoneP2P', 'InputPrivacyKeyPhoneP2P'] = pydantic.Field(
        'types.InputPrivacyKeyPhoneP2P',
        alias='_'
    )

