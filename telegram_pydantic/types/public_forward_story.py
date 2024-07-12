from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PublicForwardStory(BaseModel):
    """
    types.PublicForwardStory
    ID: 0xedf3add0
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PublicForwardStory', 'PublicForwardStory'] = pydantic.Field(
        'types.PublicForwardStory',
        alias='_'
    )

    peer: "base.Peer"
    story: "base.StoryItem"
