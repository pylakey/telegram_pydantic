from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StickerKeyword(BaseModel):
    """
    types.StickerKeyword
    ID: 0xfcfeb29c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StickerKeyword', 'StickerKeyword'] = pydantic.Field(
        'types.StickerKeyword',
        alias='_'
    )

    document_id: int
    keyword: list[str]
