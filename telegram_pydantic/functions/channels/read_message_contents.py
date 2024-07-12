from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReadMessageContents(BaseModel):
    """
    functions.channels.ReadMessageContents
    ID: 0xeab5dc38
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.ReadMessageContents', 'ReadMessageContents'] = pydantic.Field(
        'functions.channels.ReadMessageContents',
        alias='_'
    )

    channel: "base.InputChannel"
    id: list[int]
