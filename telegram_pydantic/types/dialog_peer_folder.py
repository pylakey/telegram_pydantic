from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DialogPeerFolder(BaseModel):
    """
    types.DialogPeerFolder
    ID: 0x514519e2
    Layer: 181
    """
    QUALNAME: typing.Literal['types.DialogPeerFolder', 'DialogPeerFolder'] = pydantic.Field(
        'types.DialogPeerFolder',
        alias='_'
    )

    folder_id: int
