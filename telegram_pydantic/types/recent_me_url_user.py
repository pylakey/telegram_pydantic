from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class RecentMeUrlUser(BaseModel):
    """
    types.RecentMeUrlUser
    ID: 0xb92c09e2
    Layer: 181
    """
    QUALNAME: typing.Literal['types.RecentMeUrlUser', 'RecentMeUrlUser'] = pydantic.Field(
        'types.RecentMeUrlUser',
        alias='_'
    )

    url: str
    user_id: int
