from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputWebFileLocation(BaseModel):
    """
    types.InputWebFileLocation
    ID: 0xc239d686
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputWebFileLocation', 'InputWebFileLocation'] = pydantic.Field(
        'types.InputWebFileLocation',
        alias='_'
    )

    url: str
    access_hash: int
