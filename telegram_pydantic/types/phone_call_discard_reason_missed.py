from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PhoneCallDiscardReasonMissed(BaseModel):
    """
    types.PhoneCallDiscardReasonMissed
    ID: 0x85e42301
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PhoneCallDiscardReasonMissed', 'PhoneCallDiscardReasonMissed'] = pydantic.Field(
        'types.PhoneCallDiscardReasonMissed',
        alias='_'
    )

