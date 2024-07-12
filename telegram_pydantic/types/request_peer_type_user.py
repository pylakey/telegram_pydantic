from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class RequestPeerTypeUser(BaseModel):
    """
    types.RequestPeerTypeUser
    ID: 0x5f3b8a00
    Layer: 181
    """
    QUALNAME: typing.Literal['types.RequestPeerTypeUser', 'RequestPeerTypeUser'] = pydantic.Field(
        'types.RequestPeerTypeUser',
        alias='_'
    )

    bot: typing.Optional[bool] = None
    premium: typing.Optional[bool] = None
