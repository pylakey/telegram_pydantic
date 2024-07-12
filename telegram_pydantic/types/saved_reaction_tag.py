from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SavedReactionTag(BaseModel):
    """
    types.SavedReactionTag
    ID: 0xcb6ff828
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SavedReactionTag', 'SavedReactionTag'] = pydantic.Field(
        'types.SavedReactionTag',
        alias='_'
    )

    reaction: "base.Reaction"
    count: int
    title: typing.Optional[str] = None
