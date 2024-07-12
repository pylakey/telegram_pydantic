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
    functions.messages.GetMessages
    ID: 0x63c66506
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetMessages', 'GetMessages'] = pydantic.Field(
        'functions.messages.GetMessages',
        alias='_'
    )

    id: list["base.InputMessage"]
