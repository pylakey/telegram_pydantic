from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class WebPageAttributeStory(BaseModel):
    """
    types.WebPageAttributeStory
    ID: 0x2e94c3e7
    Layer: 181
    """
    QUALNAME: typing.Literal['types.WebPageAttributeStory', 'WebPageAttributeStory'] = pydantic.Field(
        'types.WebPageAttributeStory',
        alias='_'
    )

    peer: "base.Peer"
    id: int
    story: typing.Optional["base.StoryItem"] = None
