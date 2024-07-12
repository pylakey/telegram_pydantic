from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SetBotGroupDefaultAdminRights(BaseModel):
    """
    functions.bots.SetBotGroupDefaultAdminRights
    ID: 0x925ec9ea
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.bots.SetBotGroupDefaultAdminRights', 'SetBotGroupDefaultAdminRights'] = pydantic.Field(
        'functions.bots.SetBotGroupDefaultAdminRights',
        alias='_'
    )

    admin_rights: "base.ChatAdminRights"
