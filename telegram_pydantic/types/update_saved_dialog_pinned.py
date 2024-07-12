from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateSavedDialogPinned(BaseModel):
    """
    types.UpdateSavedDialogPinned
    ID: 0xaeaf9e74
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateSavedDialogPinned', 'UpdateSavedDialogPinned'] = pydantic.Field(
        'types.UpdateSavedDialogPinned',
        alias='_'
    )

    peer: "base.DialogPeer"
    pinned: typing.Optional[bool] = None
