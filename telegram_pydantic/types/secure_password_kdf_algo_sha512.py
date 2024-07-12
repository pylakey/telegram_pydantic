from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecurePasswordKdfAlgoSHA512(BaseModel):
    """
    types.SecurePasswordKdfAlgoSHA512
    ID: 0x86471d92
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecurePasswordKdfAlgoSHA512', 'SecurePasswordKdfAlgoSHA512'] = pydantic.Field(
        'types.SecurePasswordKdfAlgoSHA512',
        alias='_'
    )

    salt: Bytes
