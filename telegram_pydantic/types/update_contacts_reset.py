from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateContactsReset(BaseModel):
    """
    types.UpdateContactsReset
    ID: 0x7084a7be
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateContactsReset', 'UpdateContactsReset'] = pydantic.Field(
        'types.UpdateContactsReset',
        alias='_'
    )

