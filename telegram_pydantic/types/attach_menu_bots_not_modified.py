from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AttachMenuBotsNotModified(BaseModel):
    """
    types.AttachMenuBotsNotModified
    ID: 0xf1d88a5c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.AttachMenuBotsNotModified', 'AttachMenuBotsNotModified'] = pydantic.Field(
        'types.AttachMenuBotsNotModified',
        alias='_'
    )

