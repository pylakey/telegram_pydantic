from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetNotifyExceptions(BaseModel):
    """
    functions.account.GetNotifyExceptions
    ID: 0x53577479
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.GetNotifyExceptions', 'GetNotifyExceptions'] = pydantic.Field(
        'functions.account.GetNotifyExceptions',
        alias='_'
    )

    compare_sound: typing.Optional[bool] = None
    compare_stories: typing.Optional[bool] = None
    peer: typing.Optional["base.InputNotifyPeer"] = None
