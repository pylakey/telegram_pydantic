from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ConnectedBot(BaseModel):
    """
    types.ConnectedBot
    ID: 0xbd068601
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ConnectedBot', 'ConnectedBot'] = pydantic.Field(
        'types.ConnectedBot',
        alias='_'
    )

    bot_id: int
    recipients: "base.BusinessBotRecipients"
    can_reply: typing.Optional[bool] = None
