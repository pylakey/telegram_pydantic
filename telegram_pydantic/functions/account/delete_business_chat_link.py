from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DeleteBusinessChatLink(BaseModel):
    """
    functions.account.DeleteBusinessChatLink
    ID: 0x60073674
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.DeleteBusinessChatLink', 'DeleteBusinessChatLink'] = pydantic.Field(
        'functions.account.DeleteBusinessChatLink',
        alias='_'
    )

    slug: str
