from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ContactStatus(BaseModel):
    """
    types.ContactStatus
    ID: 0x16d9703b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ContactStatus', 'ContactStatus'] = pydantic.Field(
        'types.ContactStatus',
        alias='_'
    )

    user_id: int
    status: "base.UserStatus"
