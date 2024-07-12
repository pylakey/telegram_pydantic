from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputBotAppShortName(BaseModel):
    """
    types.InputBotAppShortName
    ID: 0x908c0407
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputBotAppShortName', 'InputBotAppShortName'] = pydantic.Field(
        'types.InputBotAppShortName',
        alias='_'
    )

    bot_id: "base.InputUser"
    short_name: str
