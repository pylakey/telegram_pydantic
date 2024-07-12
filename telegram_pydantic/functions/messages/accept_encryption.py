from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AcceptEncryption(BaseModel):
    """
    functions.messages.AcceptEncryption
    ID: 0x3dbc0415
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.AcceptEncryption', 'AcceptEncryption'] = pydantic.Field(
        'functions.messages.AcceptEncryption',
        alias='_'
    )

    peer: "base.InputEncryptedChat"
    g_b: Bytes
    key_fingerprint: int
