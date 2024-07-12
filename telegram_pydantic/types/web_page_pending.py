from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class WebPagePending(BaseModel):
    """
    types.WebPagePending
    ID: 0xb0d13e47
    Layer: 181
    """
    QUALNAME: typing.Literal['types.WebPagePending', 'WebPagePending'] = pydantic.Field(
        'types.WebPagePending',
        alias='_'
    )

    id: int
    date: Datetime
    url: typing.Optional[str] = None
