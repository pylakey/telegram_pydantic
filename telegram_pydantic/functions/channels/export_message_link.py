from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ExportMessageLink(BaseModel):
    """
    functions.channels.ExportMessageLink
    ID: 0xe63fadeb
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.ExportMessageLink', 'ExportMessageLink'] = pydantic.Field(
        'functions.channels.ExportMessageLink',
        alias='_'
    )

    channel: "base.InputChannel"
    id: int
    grouped: typing.Optional[bool] = None
    thread: typing.Optional[bool] = None
