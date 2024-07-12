from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StoryView(BaseModel):
    """
    types.StoryView
    ID: 0xb0bdeac5
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StoryView', 'StoryView'] = pydantic.Field(
        'types.StoryView',
        alias='_'
    )

    user_id: int
    date: Datetime
    blocked: typing.Optional[bool] = None
    blocked_my_stories_from: typing.Optional[bool] = None
    reaction: typing.Optional["base.Reaction"] = None
