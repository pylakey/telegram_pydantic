from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetDeepLinkInfo(BaseModel):
    """
    functions.help.GetDeepLinkInfo
    ID: 0x3fedc75f
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.help.GetDeepLinkInfo', 'GetDeepLinkInfo'] = pydantic.Field(
        'functions.help.GetDeepLinkInfo',
        alias='_'
    )

    path: str
