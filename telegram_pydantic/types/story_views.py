from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StoryViews(BaseModel):
    """
    types.StoryViews
    ID: 0x8d595cd6
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StoryViews', 'StoryViews'] = pydantic.Field(
        'types.StoryViews',
        alias='_'
    )

    views_count: int
    has_viewers: typing.Optional[bool] = None
    forwards_count: typing.Optional[int] = None
    reactions: typing.Optional[list["base.ReactionCount"]] = None
    reactions_count: typing.Optional[int] = None
    recent_viewers: typing.Optional[list[int]] = None
