from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetWebAuthorizations(BaseModel):
    """
    functions.account.GetWebAuthorizations
    ID: 0x182e6d6f
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.GetWebAuthorizations', 'GetWebAuthorizations'] = pydantic.Field(
        'functions.account.GetWebAuthorizations',
        alias='_'
    )

