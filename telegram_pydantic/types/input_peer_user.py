from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPeerUser(BaseModel):
    """
    types.InputPeerUser
    ID: 0xdde8a54c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPeerUser', 'InputPeerUser'] = pydantic.Field(
        'types.InputPeerUser',
        alias='_'
    )

    user_id: int
    access_hash: int
