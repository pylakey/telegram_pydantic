from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputGroupCall(BaseModel):
    """
    types.InputGroupCall
    ID: 0xd8aa840f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputGroupCall', 'InputGroupCall'] = pydantic.Field(
        'types.InputGroupCall',
        alias='_'
    )

    id: int
    access_hash: int
