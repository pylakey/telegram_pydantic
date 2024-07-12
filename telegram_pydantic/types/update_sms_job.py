from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateSmsJob(BaseModel):
    """
    types.UpdateSmsJob
    ID: 0xf16269d4
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateSmsJob', 'UpdateSmsJob'] = pydantic.Field(
        'types.UpdateSmsJob',
        alias='_'
    )

    job_id: str
