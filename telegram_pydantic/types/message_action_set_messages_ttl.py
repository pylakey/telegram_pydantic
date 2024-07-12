from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionSetMessagesTTL(BaseModel):
    """
    types.MessageActionSetMessagesTTL
    ID: 0x3c134d7b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionSetMessagesTTL', 'MessageActionSetMessagesTTL'] = pydantic.Field(
        'types.MessageActionSetMessagesTTL',
        alias='_'
    )

    period: int
    auto_setting_from: typing.Optional[int] = None
