from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetStatus(BaseModel):
    """
    functions.smsjobs.GetStatus
    ID: 0x10a698e8
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.smsjobs.GetStatus', 'GetStatus'] = pydantic.Field(
        'functions.smsjobs.GetStatus',
        alias='_'
    )

