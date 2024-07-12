from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageReplyStoryHeader(BaseModel):
    """
    types.MessageReplyStoryHeader
    ID: 0xe5af939
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageReplyStoryHeader', 'MessageReplyStoryHeader'] = pydantic.Field(
        'types.MessageReplyStoryHeader',
        alias='_'
    )

    peer: "base.Peer"
    story_id: int
