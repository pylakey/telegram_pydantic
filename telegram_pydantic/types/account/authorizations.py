from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Authorizations(BaseModel):
    """
    types.account.Authorizations
    ID: 0x4bff8ea0
    Layer: 181
    """
    QUALNAME: typing.Literal['types.account.Authorizations', 'Authorizations'] = pydantic.Field(
        'types.account.Authorizations',
        alias='_'
    )

    authorization_ttl_days: int
    authorizations: list["base.Authorization"]
