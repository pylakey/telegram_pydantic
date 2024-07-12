from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetGroupCallStreamChannels(BaseModel):
    """
    functions.phone.GetGroupCallStreamChannels
    ID: 0x1ab21940
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.phone.GetGroupCallStreamChannels', 'GetGroupCallStreamChannels'] = pydantic.Field(
        'functions.phone.GetGroupCallStreamChannels',
        alias='_'
    )

    call: "base.InputGroupCall"
