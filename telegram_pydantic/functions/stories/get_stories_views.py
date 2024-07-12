from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetStoriesViews(BaseModel):
    """
    functions.stories.GetStoriesViews
    ID: 0x28e16cc8
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stories.GetStoriesViews', 'GetStoriesViews'] = pydantic.Field(
        'functions.stories.GetStoriesViews',
        alias='_'
    )

    peer: "base.InputPeer"
    id: list[int]
