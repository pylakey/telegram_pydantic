from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendEncrypted(BaseModel):
    """
    functions.messages.SendEncrypted
    ID: 0x44fa7a15
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.SendEncrypted', 'SendEncrypted'] = pydantic.Field(
        'functions.messages.SendEncrypted',
        alias='_'
    )

    peer: "base.InputEncryptedChat"
    random_id: int
    data: Bytes
    silent: typing.Optional[bool] = None
