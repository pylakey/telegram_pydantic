from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TogglePinnedToTop(BaseModel):
    """
    functions.stories.TogglePinnedToTop
    ID: 0xb297e9b
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stories.TogglePinnedToTop', 'TogglePinnedToTop'] = pydantic.Field(
        'functions.stories.TogglePinnedToTop',
        alias='_'
    )

    peer: "base.InputPeer"
    id: list[int]
