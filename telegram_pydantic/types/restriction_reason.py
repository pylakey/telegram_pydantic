from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class RestrictionReason(BaseModel):
    """
    types.RestrictionReason
    ID: 0xd072acb4
    Layer: 181
    """
    QUALNAME: typing.Literal['types.RestrictionReason', 'RestrictionReason'] = pydantic.Field(
        'types.RestrictionReason',
        alias='_'
    )

    platform: str
    reason: str
    text: str
