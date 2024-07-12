from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetOnlines(BaseModel):
    """
    functions.messages.GetOnlines
    ID: 0x6e2be050
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetOnlines', 'GetOnlines'] = pydantic.Field(
        'functions.messages.GetOnlines',
        alias='_'
    )

    peer: "base.InputPeer"
