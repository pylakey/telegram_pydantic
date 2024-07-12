from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputDialogPeerFolder(BaseModel):
    """
    types.InputDialogPeerFolder
    ID: 0x64600527
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputDialogPeerFolder', 'InputDialogPeerFolder'] = pydantic.Field(
        'types.InputDialogPeerFolder',
        alias='_'
    )

    folder_id: int
