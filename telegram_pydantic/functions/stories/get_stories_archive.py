from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetStoriesArchive(BaseModel):
    """
    functions.stories.GetStoriesArchive
    ID: 0xb4352016
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stories.GetStoriesArchive', 'GetStoriesArchive'] = pydantic.Field(
        'functions.stories.GetStoriesArchive',
        alias='_'
    )

    peer: "base.InputPeer"
    offset_id: int
    limit: int
