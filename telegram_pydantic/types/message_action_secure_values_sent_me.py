from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionSecureValuesSentMe(BaseModel):
    """
    types.MessageActionSecureValuesSentMe
    ID: 0x1b287353
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionSecureValuesSentMe', 'MessageActionSecureValuesSentMe'] = pydantic.Field(
        'types.MessageActionSecureValuesSentMe',
        alias='_'
    )

    values: list["base.SecureValue"]
    credentials: "base.SecureCredentialsEncrypted"
