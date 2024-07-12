from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendReaction(BaseModel):
    """
    functions.stories.SendReaction
    ID: 0x7fd736b2
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stories.SendReaction', 'SendReaction'] = pydantic.Field(
        'functions.stories.SendReaction',
        alias='_'
    )

    peer: "base.InputPeer"
    story_id: int
    reaction: "base.Reaction"
    add_to_recent: typing.Optional[bool] = None
