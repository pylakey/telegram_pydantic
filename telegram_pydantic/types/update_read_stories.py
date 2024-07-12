from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateReadStories(BaseModel):
    """
    types.UpdateReadStories
    ID: 0xf74e932b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateReadStories', 'UpdateReadStories'] = pydantic.Field(
        'types.UpdateReadStories',
        alias='_'
    )

    peer: "base.Peer"
    max_id: int
