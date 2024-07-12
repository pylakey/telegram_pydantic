from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetAuthorizations(BaseModel):
    """
    functions.account.GetAuthorizations
    ID: 0xe320c158
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.GetAuthorizations', 'GetAuthorizations'] = pydantic.Field(
        'functions.account.GetAuthorizations',
        alias='_'
    )

