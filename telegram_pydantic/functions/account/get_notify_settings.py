from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetNotifySettings(BaseModel):
    """
    functions.account.GetNotifySettings
    ID: 0x12b3ad31
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.GetNotifySettings', 'GetNotifySettings'] = pydantic.Field(
        'functions.account.GetNotifySettings',
        alias='_'
    )

    peer: "base.InputNotifyPeer"
