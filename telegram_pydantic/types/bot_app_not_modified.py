from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BotAppNotModified(BaseModel):
    """
    types.BotAppNotModified
    ID: 0x5da674b7
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BotAppNotModified', 'BotAppNotModified'] = pydantic.Field(
        'types.BotAppNotModified',
        alias='_'
    )

