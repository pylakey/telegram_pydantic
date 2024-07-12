from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetAttachMenuBots(BaseModel):
    """
    functions.messages.GetAttachMenuBots
    ID: 0x16fcc2cb
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetAttachMenuBots', 'GetAttachMenuBots'] = pydantic.Field(
        'functions.messages.GetAttachMenuBots',
        alias='_'
    )

    hash: int
