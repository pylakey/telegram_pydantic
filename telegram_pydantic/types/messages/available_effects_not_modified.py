from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AvailableEffectsNotModified(BaseModel):
    """
    types.messages.AvailableEffectsNotModified
    ID: 0xd1ed9a5b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.AvailableEffectsNotModified', 'AvailableEffectsNotModified'] = pydantic.Field(
        'types.messages.AvailableEffectsNotModified',
        alias='_'
    )

