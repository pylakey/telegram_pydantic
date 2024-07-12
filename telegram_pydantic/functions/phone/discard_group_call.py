from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DiscardGroupCall(BaseModel):
    """
    functions.phone.DiscardGroupCall
    ID: 0x7a777135
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.phone.DiscardGroupCall', 'DiscardGroupCall'] = pydantic.Field(
        'functions.phone.DiscardGroupCall',
        alias='_'
    )

    call: "base.InputGroupCall"
