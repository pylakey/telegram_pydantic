from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputNotifyChats(BaseModel):
    """
    types.InputNotifyChats
    ID: 0x4a95e84e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputNotifyChats', 'InputNotifyChats'] = pydantic.Field(
        'types.InputNotifyChats',
        alias='_'
    )

