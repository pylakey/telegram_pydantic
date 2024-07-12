from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PostInteractionCountersStory(BaseModel):
    """
    types.PostInteractionCountersStory
    ID: 0x8a480e27
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PostInteractionCountersStory', 'PostInteractionCountersStory'] = pydantic.Field(
        'types.PostInteractionCountersStory',
        alias='_'
    )

    story_id: int
    views: int
    forwards: int
    reactions: int
