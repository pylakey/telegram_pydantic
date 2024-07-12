from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReorderUsernames(BaseModel):
    """
    functions.account.ReorderUsernames
    ID: 0xef500eab
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.ReorderUsernames', 'ReorderUsernames'] = pydantic.Field(
        'functions.account.ReorderUsernames',
        alias='_'
    )

    order: list[str]
