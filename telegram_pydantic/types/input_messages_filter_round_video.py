from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMessagesFilterRoundVideo(BaseModel):
    """
    types.InputMessagesFilterRoundVideo
    ID: 0xb549da53
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMessagesFilterRoundVideo', 'InputMessagesFilterRoundVideo'] = pydantic.Field(
        'types.InputMessagesFilterRoundVideo',
        alias='_'
    )

