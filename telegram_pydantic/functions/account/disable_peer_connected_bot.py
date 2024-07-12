from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DisablePeerConnectedBot(BaseModel):
    """
    functions.account.DisablePeerConnectedBot
    ID: 0x5e437ed9
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.DisablePeerConnectedBot', 'DisablePeerConnectedBot'] = pydantic.Field(
        'functions.account.DisablePeerConnectedBot',
        alias='_'
    )

    peer: "base.InputPeer"
