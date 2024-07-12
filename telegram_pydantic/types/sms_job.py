from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SmsJob(BaseModel):
    """
    types.SmsJob
    ID: 0xe6a1eeb8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SmsJob', 'SmsJob'] = pydantic.Field(
        'types.SmsJob',
        alias='_'
    )

    job_id: str
    phone_number: str
    text: str
