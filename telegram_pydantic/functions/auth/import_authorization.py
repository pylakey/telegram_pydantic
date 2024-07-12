from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ImportAuthorization(BaseModel):
    """
    functions.auth.ImportAuthorization
    ID: 0xa57a7dad
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.auth.ImportAuthorization', 'ImportAuthorization'] = pydantic.Field(
        'functions.auth.ImportAuthorization',
        alias='_'
    )

    id: int
    bytes: Bytes
