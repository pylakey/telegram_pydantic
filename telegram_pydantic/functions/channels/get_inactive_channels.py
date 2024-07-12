from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetInactiveChannels(BaseModel):
    """
    functions.channels.GetInactiveChannels
    ID: 0x11e831ee
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.GetInactiveChannels', 'GetInactiveChannels'] = pydantic.Field(
        'functions.channels.GetInactiveChannels',
        alias='_'
    )

