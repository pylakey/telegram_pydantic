from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class WebAuthorizations(BaseModel):
    """
    types.account.WebAuthorizations
    ID: 0xed56c9fc
    Layer: 181
    """
    QUALNAME: typing.Literal['types.account.WebAuthorizations', 'WebAuthorizations'] = pydantic.Field(
        'types.account.WebAuthorizations',
        alias='_'
    )

    authorizations: list["base.WebAuthorization"]
    users: list["base.User"]
