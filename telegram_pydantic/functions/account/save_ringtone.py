from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SaveRingtone(BaseModel):
    """
    functions.account.SaveRingtone
    ID: 0x3dea5b03
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.SaveRingtone', 'SaveRingtone'] = pydantic.Field(
        'functions.account.SaveRingtone',
        alias='_'
    )

    id: "base.InputDocument"
    unsave: bool
