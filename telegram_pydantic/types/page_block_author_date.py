from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageBlockAuthorDate(BaseModel):
    """
    types.PageBlockAuthorDate
    ID: 0xbaafe5e0
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageBlockAuthorDate', 'PageBlockAuthorDate'] = pydantic.Field(
        'types.PageBlockAuthorDate',
        alias='_'
    )

    author: "base.RichText"
    published_date: Datetime
