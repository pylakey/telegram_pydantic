from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChatInvite(BaseModel):
    """
    types.ChatInvite
    ID: 0xcde0ec40
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChatInvite', 'ChatInvite'] = pydantic.Field(
        'types.ChatInvite',
        alias='_'
    )

    title: str
    photo: "base.Photo"
    participants_count: int
    color: int
    channel: typing.Optional[bool] = None
    broadcast: typing.Optional[bool] = None
    public: typing.Optional[bool] = None
    megagroup: typing.Optional[bool] = None
    request_needed: typing.Optional[bool] = None
    verified: typing.Optional[bool] = None
    scam: typing.Optional[bool] = None
    fake: typing.Optional[bool] = None
    about: typing.Optional[str] = None
    participants: typing.Optional[list["base.User"]] = None
