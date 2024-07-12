from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateWebPage(BaseModel):
    """
    types.UpdateWebPage
    ID: 0x7f891213
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateWebPage', 'UpdateWebPage'] = pydantic.Field(
        'types.UpdateWebPage',
        alias='_'
    )

    webpage: "base.WebPage"
    pts: int
    pts_count: int
