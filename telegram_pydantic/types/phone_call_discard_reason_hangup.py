from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PhoneCallDiscardReasonHangup(BaseModel):
    """
    types.PhoneCallDiscardReasonHangup
    ID: 0x57adc690
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PhoneCallDiscardReasonHangup', 'PhoneCallDiscardReasonHangup'] = pydantic.Field(
        'types.PhoneCallDiscardReasonHangup',
        alias='_'
    )

