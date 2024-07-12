from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateFolderPeers(BaseModel):
    """
    types.UpdateFolderPeers
    ID: 0x19360dc0
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateFolderPeers', 'UpdateFolderPeers'] = pydantic.Field(
        'types.UpdateFolderPeers',
        alias='_'
    )

    folder_peers: list["base.FolderPeer"]
    pts: int
    pts_count: int
