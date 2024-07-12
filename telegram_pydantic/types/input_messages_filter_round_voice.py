from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMessagesFilterRoundVoice(BaseModel):
    """
    types.InputMessagesFilterRoundVoice
    ID: 0x7a7c17a4
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMessagesFilterRoundVoice', 'InputMessagesFilterRoundVoice'] = pydantic.Field(
        'types.InputMessagesFilterRoundVoice',
        alias='_'
    )

