from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputStickerSetShortName(BaseModel):
    """
    types.InputStickerSetShortName
    ID: 0x861cc8a0
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputStickerSetShortName', 'InputStickerSetShortName'] = pydantic.Field(
        'types.InputStickerSetShortName',
        alias='_'
    )

    short_name: str
