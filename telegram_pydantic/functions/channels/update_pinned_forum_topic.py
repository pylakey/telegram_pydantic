from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdatePinnedForumTopic(BaseModel):
    """
    functions.channels.UpdatePinnedForumTopic
    ID: 0x6c2d9026
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.UpdatePinnedForumTopic', 'UpdatePinnedForumTopic'] = pydantic.Field(
        'functions.channels.UpdatePinnedForumTopic',
        alias='_'
    )

    channel: "base.InputChannel"
    topic_id: int
    pinned: bool
