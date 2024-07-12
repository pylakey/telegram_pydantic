from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ResolveBusinessChatLink(BaseModel):
    """
    functions.account.ResolveBusinessChatLink
    ID: 0x5492e5ee
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.ResolveBusinessChatLink', 'ResolveBusinessChatLink'] = pydantic.Field(
        'functions.account.ResolveBusinessChatLink',
        alias='_'
    )

    slug: str
