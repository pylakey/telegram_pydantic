from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PrivacyValueAllowUsers(BaseModel):
    """
    types.PrivacyValueAllowUsers
    ID: 0xb8905fb2
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PrivacyValueAllowUsers', 'PrivacyValueAllowUsers'] = pydantic.Field(
        'types.PrivacyValueAllowUsers',
        alias='_'
    )

    users: list[int]
