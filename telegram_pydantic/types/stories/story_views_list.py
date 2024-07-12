from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StoryViewsList(BaseModel):
    """
    types.stories.StoryViewsList
    ID: 0x59d78fc5
    Layer: 181
    """
    QUALNAME: typing.Literal['types.stories.StoryViewsList', 'StoryViewsList'] = pydantic.Field(
        'types.stories.StoryViewsList',
        alias='_'
    )

    count: int
    views_count: int
    forwards_count: int
    reactions_count: int
    views: list["base.StoryView"]
    chats: list["base.Chat"]
    users: list["base.User"]
    next_offset: typing.Optional[str] = None
