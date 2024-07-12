from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageBlockOrderedList(BaseModel):
    """
    types.PageBlockOrderedList
    ID: 0x9a8ae1e1
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageBlockOrderedList', 'PageBlockOrderedList'] = pydantic.Field(
        'types.PageBlockOrderedList',
        alias='_'
    )

    items: list["base.PageListOrderedItem"]
