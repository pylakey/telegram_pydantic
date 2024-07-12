from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageTableRow(BaseModel):
    """
    types.PageTableRow
    ID: 0xe0c0c5e5
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageTableRow', 'PageTableRow'] = pydantic.Field(
        'types.PageTableRow',
        alias='_'
    )

    cells: list["base.PageTableCell"]
