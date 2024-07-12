from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReceivedCall(BaseModel):
    """
    functions.phone.ReceivedCall
    ID: 0x17d54f61
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.phone.ReceivedCall', 'ReceivedCall'] = pydantic.Field(
        'functions.phone.ReceivedCall',
        alias='_'
    )

    peer: "base.InputPhoneCall"
