from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ToggleForum(BaseModel):
    """
    functions.channels.ToggleForum
    ID: 0xa4298b29
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.ToggleForum', 'ToggleForum'] = pydantic.Field(
        'functions.channels.ToggleForum',
        alias='_'
    )

    channel: "base.InputChannel"
    enabled: bool
