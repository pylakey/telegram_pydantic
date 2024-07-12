from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ConvertToGigagroup(BaseModel):
    """
    functions.channels.ConvertToGigagroup
    ID: 0xb290c69
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.ConvertToGigagroup', 'ConvertToGigagroup'] = pydantic.Field(
        'functions.channels.ConvertToGigagroup',
        alias='_'
    )

    channel: "base.InputChannel"
