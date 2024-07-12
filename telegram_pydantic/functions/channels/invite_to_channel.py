from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InviteToChannel(BaseModel):
    """
    functions.channels.InviteToChannel
    ID: 0xc9e33d54
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.InviteToChannel', 'InviteToChannel'] = pydantic.Field(
        'functions.channels.InviteToChannel',
        alias='_'
    )

    channel: "base.InputChannel"
    users: list["base.InputUser"]
