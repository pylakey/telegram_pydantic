from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendEncryptedService(BaseModel):
    """
    functions.messages.SendEncryptedService
    ID: 0x32d439a4
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.SendEncryptedService', 'SendEncryptedService'] = pydantic.Field(
        'functions.messages.SendEncryptedService',
        alias='_'
    )

    peer: "base.InputEncryptedChat"
    random_id: int
    data: Bytes
