from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageListOrderedItemText(BaseModel):
    """
    types.PageListOrderedItemText
    ID: 0x5e068047
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageListOrderedItemText', 'PageListOrderedItemText'] = pydantic.Field(
        'types.PageListOrderedItemText',
        alias='_'
    )

    num: str
    text: "base.RichText"
