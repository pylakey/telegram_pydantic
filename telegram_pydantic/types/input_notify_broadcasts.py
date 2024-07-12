from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputNotifyBroadcasts(BaseModel):
    """
    types.InputNotifyBroadcasts
    ID: 0xb1db7c7e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputNotifyBroadcasts', 'InputNotifyBroadcasts'] = pydantic.Field(
        'types.InputNotifyBroadcasts',
        alias='_'
    )

