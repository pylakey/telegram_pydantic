from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReorderPinnedForumTopics(BaseModel):
    """
    functions.channels.ReorderPinnedForumTopics
    ID: 0x2950a18f
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.ReorderPinnedForumTopics', 'ReorderPinnedForumTopics'] = pydantic.Field(
        'functions.channels.ReorderPinnedForumTopics',
        alias='_'
    )

    channel: "base.InputChannel"
    order: list[int]
    force: typing.Optional[bool] = None
