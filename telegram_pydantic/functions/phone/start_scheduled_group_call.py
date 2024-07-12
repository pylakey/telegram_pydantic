from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StartScheduledGroupCall(BaseModel):
    """
    functions.phone.StartScheduledGroupCall
    ID: 0x5680e342
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.phone.StartScheduledGroupCall', 'StartScheduledGroupCall'] = pydantic.Field(
        'functions.phone.StartScheduledGroupCall',
        alias='_'
    )

    call: "base.InputGroupCall"
