from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReorderPinnedSavedDialogs(BaseModel):
    """
    functions.messages.ReorderPinnedSavedDialogs
    ID: 0x8b716587
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.ReorderPinnedSavedDialogs', 'ReorderPinnedSavedDialogs'] = pydantic.Field(
        'functions.messages.ReorderPinnedSavedDialogs',
        alias='_'
    )

    order: list["base.InputDialogPeer"]
    force: typing.Optional[bool] = None
