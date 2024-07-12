from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DeleteStories(BaseModel):
    """
    functions.stories.DeleteStories
    ID: 0xae59db5f
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stories.DeleteStories', 'DeleteStories'] = pydantic.Field(
        'functions.stories.DeleteStories',
        alias='_'
    )

    peer: "base.InputPeer"
    id: list[int]
