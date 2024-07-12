from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPrivacyValueAllowCloseFriends(BaseModel):
    """
    types.InputPrivacyValueAllowCloseFriends
    ID: 0x2f453e49
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPrivacyValueAllowCloseFriends', 'InputPrivacyValueAllowCloseFriends'] = pydantic.Field(
        'types.InputPrivacyValueAllowCloseFriends',
        alias='_'
    )

