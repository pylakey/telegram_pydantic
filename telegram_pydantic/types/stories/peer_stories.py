from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PeerStories(BaseModel):
    """
    types.stories.PeerStories
    ID: 0xcae68768
    Layer: 181
    """
    QUALNAME: typing.Literal['types.stories.PeerStories', 'PeerStories'] = pydantic.Field(
        'types.stories.PeerStories',
        alias='_'
    )

    stories: "base.PeerStories"
    chats: list["base.Chat"]
    users: list["base.User"]
