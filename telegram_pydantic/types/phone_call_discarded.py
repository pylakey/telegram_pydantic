from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PhoneCallDiscarded(BaseModel):
    """
    types.PhoneCallDiscarded
    ID: 0x50ca4de1
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PhoneCallDiscarded', 'PhoneCallDiscarded'] = pydantic.Field(
        'types.PhoneCallDiscarded',
        alias='_'
    )

    id: int
    need_rating: typing.Optional[bool] = None
    need_debug: typing.Optional[bool] = None
    video: typing.Optional[bool] = None
    reason: typing.Optional["base.PhoneCallDiscardReason"] = None
    duration: typing.Optional[int] = None
