from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SetBotBroadcastDefaultAdminRights(BaseModel):
    """
    functions.bots.SetBotBroadcastDefaultAdminRights
    ID: 0x788464e1
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.bots.SetBotBroadcastDefaultAdminRights', 'SetBotBroadcastDefaultAdminRights'] = pydantic.Field(
        'functions.bots.SetBotBroadcastDefaultAdminRights',
        alias='_'
    )

    admin_rights: "base.ChatAdminRights"
