from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BroadcastStats(BaseModel):
    """
    types.stats.BroadcastStats
    ID: 0x396ca5fc
    Layer: 181
    """
    QUALNAME: typing.Literal['types.stats.BroadcastStats', 'BroadcastStats'] = pydantic.Field(
        'types.stats.BroadcastStats',
        alias='_'
    )

    period: "base.StatsDateRangeDays"
    followers: "base.StatsAbsValueAndPrev"
    views_per_post: "base.StatsAbsValueAndPrev"
    shares_per_post: "base.StatsAbsValueAndPrev"
    reactions_per_post: "base.StatsAbsValueAndPrev"
    views_per_story: "base.StatsAbsValueAndPrev"
    shares_per_story: "base.StatsAbsValueAndPrev"
    reactions_per_story: "base.StatsAbsValueAndPrev"
    enabled_notifications: "base.StatsPercentValue"
    growth_graph: "base.StatsGraph"
    followers_graph: "base.StatsGraph"
    mute_graph: "base.StatsGraph"
    top_hours_graph: "base.StatsGraph"
    interactions_graph: "base.StatsGraph"
    iv_interactions_graph: "base.StatsGraph"
    views_by_source_graph: "base.StatsGraph"
    new_followers_by_source_graph: "base.StatsGraph"
    languages_graph: "base.StatsGraph"
    reactions_by_emotion_graph: "base.StatsGraph"
    story_interactions_graph: "base.StatsGraph"
    story_reactions_by_emotion_graph: "base.StatsGraph"
    recent_posts_interactions: list["base.PostInteractionCounters"]
