from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Support(BaseModel):
    """
    types.help.Support
    ID: 0x17c6b5f6
    Layer: 181
    """
    QUALNAME: typing.Literal['types.help.Support', 'Support'] = pydantic.Field(
        'types.help.Support',
        alias='_'
    )

    phone_number: str
    user: "base.User"
