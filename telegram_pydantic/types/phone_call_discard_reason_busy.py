from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PhoneCallDiscardReasonBusy(BaseModel):
    """
    types.PhoneCallDiscardReasonBusy
    ID: 0xfaf7e8c9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PhoneCallDiscardReasonBusy', 'PhoneCallDiscardReasonBusy'] = pydantic.Field(
        'types.PhoneCallDiscardReasonBusy',
        alias='_'
    )

