from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetPinnedStories(BaseModel):
    """
    functions.stories.GetPinnedStories
    ID: 0x5821a5dc
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stories.GetPinnedStories', 'GetPinnedStories'] = pydantic.Field(
        'functions.stories.GetPinnedStories',
        alias='_'
    )

    peer: "base.InputPeer"
    offset_id: int
    limit: int
