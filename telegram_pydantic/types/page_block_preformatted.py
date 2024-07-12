from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageBlockPreformatted(BaseModel):
    """
    types.PageBlockPreformatted
    ID: 0xc070d93e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageBlockPreformatted', 'PageBlockPreformatted'] = pydantic.Field(
        'types.PageBlockPreformatted',
        alias='_'
    )

    text: "base.RichText"
    language: str
