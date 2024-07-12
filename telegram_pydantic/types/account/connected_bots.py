from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ConnectedBots(BaseModel):
    """
    types.account.ConnectedBots
    ID: 0x17d7f87b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.account.ConnectedBots', 'ConnectedBots'] = pydantic.Field(
        'types.account.ConnectedBots',
        alias='_'
    )

    connected_bots: list["base.ConnectedBot"]
    users: list["base.User"]
