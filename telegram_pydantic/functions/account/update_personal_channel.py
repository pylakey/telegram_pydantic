from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdatePersonalChannel(BaseModel):
    """
    functions.account.UpdatePersonalChannel
    ID: 0xd94305e0
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.UpdatePersonalChannel', 'UpdatePersonalChannel'] = pydantic.Field(
        'functions.account.UpdatePersonalChannel',
        alias='_'
    )

    channel: "base.InputChannel"
