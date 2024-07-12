from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputSecureFile(BaseModel):
    """
    types.InputSecureFile
    ID: 0x5367e5be
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputSecureFile', 'InputSecureFile'] = pydantic.Field(
        'types.InputSecureFile',
        alias='_'
    )

    id: int
    access_hash: int
