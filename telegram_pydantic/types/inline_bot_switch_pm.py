from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InlineBotSwitchPM(BaseModel):
    """
    types.InlineBotSwitchPM
    ID: 0x3c20629f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InlineBotSwitchPM', 'InlineBotSwitchPM'] = pydantic.Field(
        'types.InlineBotSwitchPM',
        alias='_'
    )

    text: str
    start_param: str
