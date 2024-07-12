from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ToggleViewForumAsMessages(BaseModel):
    """
    functions.channels.ToggleViewForumAsMessages
    ID: 0x9738bb15
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.ToggleViewForumAsMessages', 'ToggleViewForumAsMessages'] = pydantic.Field(
        'functions.channels.ToggleViewForumAsMessages',
        alias='_'
    )

    channel: "base.InputChannel"
    enabled: bool
