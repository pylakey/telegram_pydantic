from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class WebAuthorization(BaseModel):
    """
    types.WebAuthorization
    ID: 0xa6f8f452
    Layer: 181
    """
    QUALNAME: typing.Literal['types.WebAuthorization', 'WebAuthorization'] = pydantic.Field(
        'types.WebAuthorization',
        alias='_'
    )

    hash: int
    bot_id: int
    domain: str
    browser: str
    platform: str
    date_created: Datetime
    date_active: Datetime
    ip: str
    region: str
