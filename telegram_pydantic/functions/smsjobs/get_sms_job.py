from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetSmsJob(BaseModel):
    """
    functions.smsjobs.GetSmsJob
    ID: 0x778d902f
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.smsjobs.GetSmsJob', 'GetSmsJob'] = pydantic.Field(
        'functions.smsjobs.GetSmsJob',
        alias='_'
    )

    job_id: str
