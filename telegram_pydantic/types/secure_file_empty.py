from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecureFileEmpty(BaseModel):
    """
    types.SecureFileEmpty
    ID: 0x64199744
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecureFileEmpty', 'SecureFileEmpty'] = pydantic.Field(
        'types.SecureFileEmpty',
        alias='_'
    )

