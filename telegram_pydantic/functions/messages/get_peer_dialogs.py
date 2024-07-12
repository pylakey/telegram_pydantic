from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetPeerDialogs(BaseModel):
    """
    functions.messages.GetPeerDialogs
    ID: 0xe470bcfd
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetPeerDialogs', 'GetPeerDialogs'] = pydantic.Field(
        'functions.messages.GetPeerDialogs',
        alias='_'
    )

    peers: list["base.InputDialogPeer"]
