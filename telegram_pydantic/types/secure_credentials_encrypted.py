from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecureCredentialsEncrypted(BaseModel):
    """
    types.SecureCredentialsEncrypted
    ID: 0x33f0ea47
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecureCredentialsEncrypted', 'SecureCredentialsEncrypted'] = pydantic.Field(
        'types.SecureCredentialsEncrypted',
        alias='_'
    )

    data: Bytes
    hash: Bytes
    secret: Bytes
