from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SetEncryptedTyping(BaseModel):
    """
    functions.messages.SetEncryptedTyping
    ID: 0x791451ed
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.SetEncryptedTyping', 'SetEncryptedTyping'] = pydantic.Field(
        'functions.messages.SetEncryptedTyping',
        alias='_'
    )

    peer: "base.InputEncryptedChat"
    typing: bool
