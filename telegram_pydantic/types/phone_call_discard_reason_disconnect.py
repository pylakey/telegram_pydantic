from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PhoneCallDiscardReasonDisconnect(BaseModel):
    """
    types.PhoneCallDiscardReasonDisconnect
    ID: 0xe095c1a0
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PhoneCallDiscardReasonDisconnect', 'PhoneCallDiscardReasonDisconnect'] = pydantic.Field(
        'types.PhoneCallDiscardReasonDisconnect',
        alias='_'
    )

