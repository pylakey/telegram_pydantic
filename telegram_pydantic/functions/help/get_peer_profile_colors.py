from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetPeerProfileColors(BaseModel):
    """
    functions.help.GetPeerProfileColors
    ID: 0xabcfa9fd
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.help.GetPeerProfileColors', 'GetPeerProfileColors'] = pydantic.Field(
        'functions.help.GetPeerProfileColors',
        alias='_'
    )

    hash: int
