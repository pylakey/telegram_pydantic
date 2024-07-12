from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StoryReaction(BaseModel):
    """
    types.StoryReaction
    ID: 0x6090d6d5
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StoryReaction', 'StoryReaction'] = pydantic.Field(
        'types.StoryReaction',
        alias='_'
    )

    peer_id: "base.Peer"
    date: Datetime
    reaction: "base.Reaction"
