from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StoryStats(BaseModel):
    """
    types.stats.StoryStats
    ID: 0x50cd067c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.stats.StoryStats', 'StoryStats'] = pydantic.Field(
        'types.stats.StoryStats',
        alias='_'
    )

    views_graph: "base.StatsGraph"
    reactions_by_emotion_graph: "base.StatsGraph"
