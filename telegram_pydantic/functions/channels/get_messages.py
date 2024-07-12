from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetMessages(BaseModel):
    """
    functions.channels.GetMessages
    ID: 0xad8c9a23
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.GetMessages', 'GetMessages'] = pydantic.Field(
        'functions.channels.GetMessages',
        alias='_'
    )

    channel: "base.InputChannel"
    id: list["base.InputMessage"]
