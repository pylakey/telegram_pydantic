from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AdminLogResults(BaseModel):
    """
    types.channels.AdminLogResults
    ID: 0xed8af74d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.channels.AdminLogResults', 'AdminLogResults'] = pydantic.Field(
        'types.channels.AdminLogResults',
        alias='_'
    )

    events: list["base.ChannelAdminLogEvent"]
    chats: list["base.Chat"]
    users: list["base.User"]
