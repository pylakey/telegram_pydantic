from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Status(BaseModel):
    """
    types.smsjobs.Status
    ID: 0x2aee9191
    Layer: 181
    """
    QUALNAME: typing.Literal['types.smsjobs.Status', 'Status'] = pydantic.Field(
        'types.smsjobs.Status',
        alias='_'
    )

    recent_sent: int
    recent_since: Datetime
    recent_remains: int
    total_sent: int
    total_since: Datetime
    terms_url: str
    allow_international: typing.Optional[bool] = None
    last_gift_slug: typing.Optional[str] = None
