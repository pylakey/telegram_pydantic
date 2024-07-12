from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReorderPinnedDialogs(BaseModel):
    """
    functions.messages.ReorderPinnedDialogs
    ID: 0x3b1adf37
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.ReorderPinnedDialogs', 'ReorderPinnedDialogs'] = pydantic.Field(
        'functions.messages.ReorderPinnedDialogs',
        alias='_'
    )

    folder_id: int
    order: list["base.InputDialogPeer"]
    force: typing.Optional[bool] = None
