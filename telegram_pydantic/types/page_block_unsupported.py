from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageBlockUnsupported(BaseModel):
    """
    types.PageBlockUnsupported
    ID: 0x13567e8a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageBlockUnsupported', 'PageBlockUnsupported'] = pydantic.Field(
        'types.PageBlockUnsupported',
        alias='_'
    )

