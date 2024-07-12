from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateBusinessWorkHours(BaseModel):
    """
    functions.account.UpdateBusinessWorkHours
    ID: 0x4b00e066
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.UpdateBusinessWorkHours', 'UpdateBusinessWorkHours'] = pydantic.Field(
        'functions.account.UpdateBusinessWorkHours',
        alias='_'
    )

    business_work_hours: typing.Optional["base.BusinessWorkHours"] = None
