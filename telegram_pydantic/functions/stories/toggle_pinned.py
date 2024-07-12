from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TogglePinned(BaseModel):
    """
    functions.stories.TogglePinned
    ID: 0x9a75a1ef
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stories.TogglePinned', 'TogglePinned'] = pydantic.Field(
        'functions.stories.TogglePinned',
        alias='_'
    )

    peer: "base.InputPeer"
    id: list[int]
    pinned: bool
