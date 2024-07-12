from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageTableCell(BaseModel):
    """
    types.PageTableCell
    ID: 0x34566b6a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageTableCell', 'PageTableCell'] = pydantic.Field(
        'types.PageTableCell',
        alias='_'
    )

    header: typing.Optional[bool] = None
    align_center: typing.Optional[bool] = None
    align_right: typing.Optional[bool] = None
    valign_middle: typing.Optional[bool] = None
    valign_bottom: typing.Optional[bool] = None
    text: typing.Optional["base.RichText"] = None
    colspan: typing.Optional[int] = None
    rowspan: typing.Optional[int] = None
