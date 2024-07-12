from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BotCommandScopeChatAdmins(BaseModel):
    """
    types.BotCommandScopeChatAdmins
    ID: 0xb9aa606a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BotCommandScopeChatAdmins', 'BotCommandScopeChatAdmins'] = pydantic.Field(
        'types.BotCommandScopeChatAdmins',
        alias='_'
    )

