from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetPeerMaxIDs(BaseModel):
    """
    functions.stories.GetPeerMaxIDs
    ID: 0x535983c3
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stories.GetPeerMaxIDs', 'GetPeerMaxIDs'] = pydantic.Field(
        'functions.stories.GetPeerMaxIDs',
        alias='_'
    )

    id: list["base.InputPeer"]
