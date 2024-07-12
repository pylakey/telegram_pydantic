from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ToggleStickerSets(BaseModel):
    """
    functions.messages.ToggleStickerSets
    ID: 0xb5052fea
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.ToggleStickerSets', 'ToggleStickerSets'] = pydantic.Field(
        'functions.messages.ToggleStickerSets',
        alias='_'
    )

    stickersets: list["base.InputStickerSet"]
    uninstall: typing.Optional[bool] = None
    archive: typing.Optional[bool] = None
    unarchive: typing.Optional[bool] = None
