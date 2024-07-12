from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReadDiscussion(BaseModel):
    """
    functions.messages.ReadDiscussion
    ID: 0xf731a9f4
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.ReadDiscussion', 'ReadDiscussion'] = pydantic.Field(
        'functions.messages.ReadDiscussion',
        alias='_'
    )

    peer: "base.InputPeer"
    msg_id: int
    read_max_id: int
