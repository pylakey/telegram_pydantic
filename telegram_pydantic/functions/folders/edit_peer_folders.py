from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EditPeerFolders(BaseModel):
    """
    functions.folders.EditPeerFolders
    ID: 0x6847d0ab
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.folders.EditPeerFolders', 'EditPeerFolders'] = pydantic.Field(
        'functions.folders.EditPeerFolders',
        alias='_'
    )

    folder_peers: list["base.InputFolderPeer"]
