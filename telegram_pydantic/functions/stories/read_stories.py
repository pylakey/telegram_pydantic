from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReadStories(BaseModel):
    """
    functions.stories.ReadStories
    ID: 0xa556dac8
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stories.ReadStories', 'ReadStories'] = pydantic.Field(
        'functions.stories.ReadStories',
        alias='_'
    )

    peer: "base.InputPeer"
    max_id: int
