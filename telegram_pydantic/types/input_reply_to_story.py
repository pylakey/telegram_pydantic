from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputReplyToStory(BaseModel):
    """
    types.InputReplyToStory
    ID: 0x5881323a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputReplyToStory', 'InputReplyToStory'] = pydantic.Field(
        'types.InputReplyToStory',
        alias='_'
    )

    peer: "base.InputPeer"
    story_id: int
