from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StoryReactionsList(BaseModel):
    """
    types.stories.StoryReactionsList
    ID: 0xaa5f789c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.stories.StoryReactionsList', 'StoryReactionsList'] = pydantic.Field(
        'types.stories.StoryReactionsList',
        alias='_'
    )

    count: int
    reactions: list["base.StoryReaction"]
    chats: list["base.Chat"]
    users: list["base.User"]
    next_offset: typing.Optional[str] = None
