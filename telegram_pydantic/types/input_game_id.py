from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputGameID(BaseModel):
    """
    types.InputGameID
    ID: 0x32c3e77
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputGameID', 'InputGameID'] = pydantic.Field(
        'types.InputGameID',
        alias='_'
    )

    id: int
    access_hash: int
