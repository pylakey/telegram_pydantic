from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetPeerSettings(BaseModel):
    """
    functions.messages.GetPeerSettings
    ID: 0xefd9a6a2
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetPeerSettings', 'GetPeerSettings'] = pydantic.Field(
        'functions.messages.GetPeerSettings',
        alias='_'
    )

    peer: "base.InputPeer"
