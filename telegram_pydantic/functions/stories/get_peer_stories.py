from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetPeerStories(BaseModel):
    """
    functions.stories.GetPeerStories
    ID: 0x2c4ada50
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stories.GetPeerStories', 'GetPeerStories'] = pydantic.Field(
        'functions.stories.GetPeerStories',
        alias='_'
    )

    peer: "base.InputPeer"
