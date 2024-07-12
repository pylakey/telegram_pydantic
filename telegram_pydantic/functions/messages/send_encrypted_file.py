from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendEncryptedFile(BaseModel):
    """
    functions.messages.SendEncryptedFile
    ID: 0x5559481d
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.SendEncryptedFile', 'SendEncryptedFile'] = pydantic.Field(
        'functions.messages.SendEncryptedFile',
        alias='_'
    )

    peer: "base.InputEncryptedChat"
    random_id: int
    data: Bytes
    file: "base.InputEncryptedFile"
    silent: typing.Optional[bool] = None
