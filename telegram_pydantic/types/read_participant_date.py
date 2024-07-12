from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReadParticipantDate(BaseModel):
    """
    types.ReadParticipantDate
    ID: 0x4a4ff172
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ReadParticipantDate', 'ReadParticipantDate'] = pydantic.Field(
        'types.ReadParticipantDate',
        alias='_'
    )

    user_id: int
    date: Datetime
