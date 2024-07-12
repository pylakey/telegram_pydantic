from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionGiveawayLaunch(BaseModel):
    """
    types.MessageActionGiveawayLaunch
    ID: 0x332ba9ed
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionGiveawayLaunch', 'MessageActionGiveawayLaunch'] = pydantic.Field(
        'types.MessageActionGiveawayLaunch',
        alias='_'
    )

