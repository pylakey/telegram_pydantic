from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetChatThemes(BaseModel):
    """
    functions.account.GetChatThemes
    ID: 0xd638de89
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.GetChatThemes', 'GetChatThemes'] = pydantic.Field(
        'functions.account.GetChatThemes',
        alias='_'
    )

    hash: int
