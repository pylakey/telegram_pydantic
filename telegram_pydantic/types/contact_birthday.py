from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ContactBirthday(BaseModel):
    """
    types.ContactBirthday
    ID: 0x1d998733
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ContactBirthday', 'ContactBirthday'] = pydantic.Field(
        'types.ContactBirthday',
        alias='_'
    )

    contact_id: int
    birthday: "base.Birthday"
