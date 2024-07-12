from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class FinishJob(BaseModel):
    """
    functions.smsjobs.FinishJob
    ID: 0x4f1ebf24
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.smsjobs.FinishJob', 'FinishJob'] = pydantic.Field(
        'functions.smsjobs.FinishJob',
        alias='_'
    )

    job_id: str
    error: typing.Optional[str] = None
