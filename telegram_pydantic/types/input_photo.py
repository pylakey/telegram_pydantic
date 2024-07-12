from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPhoto(BaseModel):
    """
    types.InputPhoto
    ID: 0x3bb3b94a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPhoto', 'InputPhoto'] = pydantic.Field(
        'types.InputPhoto',
        alias='_'
    )

    id: int
    access_hash: int
    file_reference: Bytes
