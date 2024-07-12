from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetWebPage(BaseModel):
    """
    functions.messages.GetWebPage
    ID: 0x8d9692a3
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetWebPage', 'GetWebPage'] = pydantic.Field(
        'functions.messages.GetWebPage',
        alias='_'
    )

    url: str
    hash: int
