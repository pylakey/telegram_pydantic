from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PrivacyValueAllowCloseFriends(BaseModel):
    """
    types.PrivacyValueAllowCloseFriends
    ID: 0xf7e8d89b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PrivacyValueAllowCloseFriends', 'PrivacyValueAllowCloseFriends'] = pydantic.Field(
        'types.PrivacyValueAllowCloseFriends',
        alias='_'
    )

