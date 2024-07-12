from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPrivacyValueAllowUsers(BaseModel):
    """
    types.InputPrivacyValueAllowUsers
    ID: 0x131cc67f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPrivacyValueAllowUsers', 'InputPrivacyValueAllowUsers'] = pydantic.Field(
        'types.InputPrivacyValueAllowUsers',
        alias='_'
    )

    users: list["base.InputUser"]
