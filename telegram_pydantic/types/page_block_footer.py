from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageBlockFooter(BaseModel):
    """
    types.PageBlockFooter
    ID: 0x48870999
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageBlockFooter', 'PageBlockFooter'] = pydantic.Field(
        'types.PageBlockFooter',
        alias='_'
    )

    text: "base.RichText"
