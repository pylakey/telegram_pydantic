from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMessagesFilterPhoneCalls(BaseModel):
    """
    types.InputMessagesFilterPhoneCalls
    ID: 0x80c99768
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMessagesFilterPhoneCalls', 'InputMessagesFilterPhoneCalls'] = pydantic.Field(
        'types.InputMessagesFilterPhoneCalls',
        alias='_'
    )

    missed: typing.Optional[bool] = None
