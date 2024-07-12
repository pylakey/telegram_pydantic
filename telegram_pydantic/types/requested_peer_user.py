from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class RequestedPeerUser(BaseModel):
    """
    types.RequestedPeerUser
    ID: 0xd62ff46a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.RequestedPeerUser', 'RequestedPeerUser'] = pydantic.Field(
        'types.RequestedPeerUser',
        alias='_'
    )

    user_id: int
    first_name: typing.Optional[str] = None
    last_name: typing.Optional[str] = None
    username: typing.Optional[str] = None
    photo: typing.Optional["base.Photo"] = None
