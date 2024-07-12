from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageStats(BaseModel):
    """
    types.stats.MessageStats
    ID: 0x7fe91c14
    Layer: 181
    """
    QUALNAME: typing.Literal['types.stats.MessageStats', 'MessageStats'] = pydantic.Field(
        'types.stats.MessageStats',
        alias='_'
    )

    views_graph: "base.StatsGraph"
    reactions_by_emotion_graph: "base.StatsGraph"
