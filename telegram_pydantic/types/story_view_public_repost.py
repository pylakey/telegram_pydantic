from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StoryViewPublicRepost(BaseModel):
    """
    types.StoryViewPublicRepost
    ID: 0xbd74cf49
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StoryViewPublicRepost', 'StoryViewPublicRepost'] = pydantic.Field(
        'types.StoryViewPublicRepost',
        alias='_'
    )

    peer_id: "base.Peer"
    story: "base.StoryItem"
    blocked: typing.Optional[bool] = None
    blocked_my_stories_from: typing.Optional[bool] = None
