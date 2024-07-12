from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageListOrderedItemBlocks(BaseModel):
    """
    types.PageListOrderedItemBlocks
    ID: 0x98dd8936
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageListOrderedItemBlocks', 'PageListOrderedItemBlocks'] = pydantic.Field(
        'types.PageListOrderedItemBlocks',
        alias='_'
    )

    num: str
    blocks: list["base.PageBlock"]
