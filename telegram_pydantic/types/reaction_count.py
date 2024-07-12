from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReactionCount(BaseModel):
    """
    types.ReactionCount
    ID: 0xa3d1cb80
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ReactionCount', 'ReactionCount'] = pydantic.Field(
        'types.ReactionCount',
        alias='_'
    )

    reaction: "base.Reaction"
    count: int
    chosen_order: typing.Optional[int] = None
