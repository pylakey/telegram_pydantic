from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMediaStory(BaseModel):
    """
    types.InputMediaStory
    ID: 0x89fdd778
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMediaStory', 'InputMediaStory'] = pydantic.Field(
        'types.InputMediaStory',
        alias='_'
    )

    peer: "base.InputPeer"
    id: int
