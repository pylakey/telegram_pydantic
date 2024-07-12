from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SavedReactionTags(BaseModel):
    """
    types.messages.SavedReactionTags
    ID: 0x3259950a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.SavedReactionTags', 'SavedReactionTags'] = pydantic.Field(
        'types.messages.SavedReactionTags',
        alias='_'
    )

    tags: list["base.SavedReactionTag"]
    hash: int
