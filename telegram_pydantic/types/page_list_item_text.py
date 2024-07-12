from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageListItemText(BaseModel):
    """
    types.PageListItemText
    ID: 0xb92fb6cd
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageListItemText', 'PageListItemText'] = pydantic.Field(
        'types.PageListItemText',
        alias='_'
    )

    text: "base.RichText"
