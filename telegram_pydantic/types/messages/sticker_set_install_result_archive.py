from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StickerSetInstallResultArchive(BaseModel):
    """
    types.messages.StickerSetInstallResultArchive
    ID: 0x35e410a8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.StickerSetInstallResultArchive', 'StickerSetInstallResultArchive'] = pydantic.Field(
        'types.messages.StickerSetInstallResultArchive',
        alias='_'
    )

    sets: list["base.StickerSetCovered"]
