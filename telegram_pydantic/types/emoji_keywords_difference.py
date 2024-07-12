from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EmojiKeywordsDifference(BaseModel):
    """
    types.EmojiKeywordsDifference
    ID: 0x5cc761bd
    Layer: 181
    """
    QUALNAME: typing.Literal['types.EmojiKeywordsDifference', 'EmojiKeywordsDifference'] = pydantic.Field(
        'types.EmojiKeywordsDifference',
        alias='_'
    )

    lang_code: str
    from_version: int
    version: int
    keywords: list["base.EmojiKeyword"]
