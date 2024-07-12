from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PhotoEmpty(BaseModel):
    """
    types.PhotoEmpty
    ID: 0x2331b22d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PhotoEmpty', 'PhotoEmpty'] = pydantic.Field(
        'types.PhotoEmpty',
        alias='_'
    )

    id: int
