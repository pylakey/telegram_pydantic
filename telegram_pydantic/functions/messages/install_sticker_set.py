from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InstallStickerSet(BaseModel):
    """
    functions.messages.InstallStickerSet
    ID: 0xc78fe460
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.InstallStickerSet', 'InstallStickerSet'] = pydantic.Field(
        'functions.messages.InstallStickerSet',
        alias='_'
    )

    stickerset: "base.InputStickerSet"
    archived: bool
