from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TimezonesListNotModified(BaseModel):
    """
    types.help.TimezonesListNotModified
    ID: 0x970708cc
    Layer: 181
    """
    QUALNAME: typing.Literal['types.help.TimezonesListNotModified', 'TimezonesListNotModified'] = pydantic.Field(
        'types.help.TimezonesListNotModified',
        alias='_'
    )

