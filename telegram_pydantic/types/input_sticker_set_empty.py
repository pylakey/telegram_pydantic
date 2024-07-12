from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputStickerSetEmpty(BaseModel):
    """
    types.InputStickerSetEmpty
    ID: 0xffb62b95
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputStickerSetEmpty', 'InputStickerSetEmpty'] = pydantic.Field(
        'types.InputStickerSetEmpty',
        alias='_'
    )

