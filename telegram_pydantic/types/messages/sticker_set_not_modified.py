from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StickerSetNotModified(BaseModel):
    """
    types.messages.StickerSetNotModified
    ID: 0xd3f924eb
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.StickerSetNotModified', 'StickerSetNotModified'] = pydantic.Field(
        'types.messages.StickerSetNotModified',
        alias='_'
    )

