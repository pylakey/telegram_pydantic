from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SetAuthorizationTTL(BaseModel):
    """
    functions.account.SetAuthorizationTTL
    ID: 0xbf899aa0
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.SetAuthorizationTTL', 'SetAuthorizationTTL'] = pydantic.Field(
        'functions.account.SetAuthorizationTTL',
        alias='_'
    )

    authorization_ttl_days: int
