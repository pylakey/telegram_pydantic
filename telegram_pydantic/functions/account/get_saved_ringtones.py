from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetSavedRingtones(BaseModel):
    """
    functions.account.GetSavedRingtones
    ID: 0xe1902288
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.GetSavedRingtones', 'GetSavedRingtones'] = pydantic.Field(
        'functions.account.GetSavedRingtones',
        alias='_'
    )

    hash: int
