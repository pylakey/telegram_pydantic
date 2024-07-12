from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChatInviteImporter(BaseModel):
    """
    types.ChatInviteImporter
    ID: 0x8c5adfd9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChatInviteImporter', 'ChatInviteImporter'] = pydantic.Field(
        'types.ChatInviteImporter',
        alias='_'
    )

    user_id: int
    date: Datetime
    requested: typing.Optional[bool] = None
    via_chatlist: typing.Optional[bool] = None
    about: typing.Optional[str] = None
    approved_by: typing.Optional[int] = None
