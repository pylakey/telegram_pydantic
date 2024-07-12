from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionGiveawayResults(BaseModel):
    """
    types.MessageActionGiveawayResults
    ID: 0x2a9fadc5
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionGiveawayResults', 'MessageActionGiveawayResults'] = pydantic.Field(
        'types.MessageActionGiveawayResults',
        alias='_'
    )

    winners_count: int
    unclaimed_count: int
