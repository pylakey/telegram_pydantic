from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateStoriesStealthMode(BaseModel):
    """
    types.UpdateStoriesStealthMode
    ID: 0x2c084dc1
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateStoriesStealthMode', 'UpdateStoriesStealthMode'] = pydantic.Field(
        'types.UpdateStoriesStealthMode',
        alias='_'
    )

    stealth_mode: "base.StoriesStealthMode"
