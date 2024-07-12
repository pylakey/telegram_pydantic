from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageListItemBlocks(BaseModel):
    """
    types.PageListItemBlocks
    ID: 0x25e073fc
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageListItemBlocks', 'PageListItemBlocks'] = pydantic.Field(
        'types.PageListItemBlocks',
        alias='_'
    )

    blocks: list["base.PageBlock"]
