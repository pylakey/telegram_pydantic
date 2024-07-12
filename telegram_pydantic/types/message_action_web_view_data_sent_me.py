from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionWebViewDataSentMe(BaseModel):
    """
    types.MessageActionWebViewDataSentMe
    ID: 0x47dd8079
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionWebViewDataSentMe', 'MessageActionWebViewDataSentMe'] = pydantic.Field(
        'types.MessageActionWebViewDataSentMe',
        alias='_'
    )

    text: str
    data: str
