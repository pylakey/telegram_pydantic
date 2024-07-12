from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ToggleSignatures(BaseModel):
    """
    functions.channels.ToggleSignatures
    ID: 0x1f69b606
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.ToggleSignatures', 'ToggleSignatures'] = pydantic.Field(
        'functions.channels.ToggleSignatures',
        alias='_'
    )

    channel: "base.InputChannel"
    enabled: bool
