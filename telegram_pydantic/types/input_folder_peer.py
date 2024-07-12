from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputFolderPeer(BaseModel):
    """
    types.InputFolderPeer
    ID: 0xfbd2c296
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputFolderPeer', 'InputFolderPeer'] = pydantic.Field(
        'types.InputFolderPeer',
        alias='_'
    )

    peer: "base.InputPeer"
    folder_id: int
