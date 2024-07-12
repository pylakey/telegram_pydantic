from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReactionEmpty(BaseModel):
    """
    types.ReactionEmpty
    ID: 0x79f5d419
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ReactionEmpty', 'ReactionEmpty'] = pydantic.Field(
        'types.ReactionEmpty',
        alias='_'
    )

