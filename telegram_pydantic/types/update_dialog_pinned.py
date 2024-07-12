from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateDialogPinned(BaseModel):
    """
    types.UpdateDialogPinned
    ID: 0x6e6fe51c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateDialogPinned', 'UpdateDialogPinned'] = pydantic.Field(
        'types.UpdateDialogPinned',
        alias='_'
    )

    peer: "base.DialogPeer"
    pinned: typing.Optional[bool] = None
    folder_id: typing.Optional[int] = None
