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
    functions.bots.ReorderUsernames
    ID: 0x9709b1c2
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.bots.ReorderUsernames', 'ReorderUsernames'] = pydantic.Field(
        'functions.bots.ReorderUsernames',
        alias='_'
    )

    bot: "base.InputUser"
    order: list[str]
