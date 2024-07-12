from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageMediaStory(BaseModel):
    """
    types.MessageMediaStory
    ID: 0x68cb6283
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageMediaStory', 'MessageMediaStory'] = pydantic.Field(
        'types.MessageMediaStory',
        alias='_'
    )

    peer: "base.Peer"
    id: int
    via_mention: typing.Optional[bool] = None
    story: typing.Optional["base.StoryItem"] = None
