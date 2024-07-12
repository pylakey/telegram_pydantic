from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionWebViewDataSent(BaseModel):
    """
    types.MessageActionWebViewDataSent
    ID: 0xb4c38cb5
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionWebViewDataSent', 'MessageActionWebViewDataSent'] = pydantic.Field(
        'types.MessageActionWebViewDataSent',
        alias='_'
    )

    text: str
