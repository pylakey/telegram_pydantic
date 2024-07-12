from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPrivacyValueDisallowUsers(BaseModel):
    """
    types.InputPrivacyValueDisallowUsers
    ID: 0x90110467
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPrivacyValueDisallowUsers', 'InputPrivacyValueDisallowUsers'] = pydantic.Field(
        'types.InputPrivacyValueDisallowUsers',
        alias='_'
    )

    users: list["base.InputUser"]
