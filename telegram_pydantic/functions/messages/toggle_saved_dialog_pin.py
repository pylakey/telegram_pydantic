from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ToggleSavedDialogPin(BaseModel):
    """
    functions.messages.ToggleSavedDialogPin
    ID: 0xac81bbde
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.ToggleSavedDialogPin', 'ToggleSavedDialogPin'] = pydantic.Field(
        'functions.messages.ToggleSavedDialogPin',
        alias='_'
    )

    peer: "base.InputDialogPeer"
    pinned: typing.Optional[bool] = None
