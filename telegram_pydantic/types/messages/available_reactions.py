from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AvailableReactions(BaseModel):
    """
    types.messages.AvailableReactions
    ID: 0x768e3aad
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.AvailableReactions', 'AvailableReactions'] = pydantic.Field(
        'types.messages.AvailableReactions',
        alias='_'
    )

    hash: int
    reactions: list["base.AvailableReaction"]
