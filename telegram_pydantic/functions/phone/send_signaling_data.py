from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendSignalingData(BaseModel):
    """
    functions.phone.SendSignalingData
    ID: 0xff7a9383
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.phone.SendSignalingData', 'SendSignalingData'] = pydantic.Field(
        'functions.phone.SendSignalingData',
        alias='_'
    )

    peer: "base.InputPhoneCall"
    data: Bytes
