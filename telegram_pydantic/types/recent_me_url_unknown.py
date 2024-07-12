from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class RecentMeUrlUnknown(BaseModel):
    """
    types.RecentMeUrlUnknown
    ID: 0x46e1d13d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.RecentMeUrlUnknown', 'RecentMeUrlUnknown'] = pydantic.Field(
        'types.RecentMeUrlUnknown',
        alias='_'
    )

    url: str
