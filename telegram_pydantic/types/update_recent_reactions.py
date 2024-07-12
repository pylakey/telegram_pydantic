from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateRecentReactions(BaseModel):
    """
    types.UpdateRecentReactions
    ID: 0x6f7863f4
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateRecentReactions', 'UpdateRecentReactions'] = pydantic.Field(
        'types.UpdateRecentReactions',
        alias='_'
    )

