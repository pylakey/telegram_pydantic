from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StoriesStealthMode(BaseModel):
    """
    types.StoriesStealthMode
    ID: 0x712e27fd
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StoriesStealthMode', 'StoriesStealthMode'] = pydantic.Field(
        'types.StoriesStealthMode',
        alias='_'
    )

    active_until_date: Datetime
    cooldown_until_date: Datetime
