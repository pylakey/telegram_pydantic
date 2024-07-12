from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputStickerSetID(BaseModel):
    """
    types.InputStickerSetID
    ID: 0x9de7a269
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputStickerSetID', 'InputStickerSetID'] = pydantic.Field(
        'types.InputStickerSetID',
        alias='_'
    )

    id: int
    access_hash: int
