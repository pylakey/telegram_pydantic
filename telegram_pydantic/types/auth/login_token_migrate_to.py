from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class LoginTokenMigrateTo(BaseModel):
    """
    types.auth.LoginTokenMigrateTo
    ID: 0x68e9916
    Layer: 181
    """
    QUALNAME: typing.Literal['types.auth.LoginTokenMigrateTo', 'LoginTokenMigrateTo'] = pydantic.Field(
        'types.auth.LoginTokenMigrateTo',
        alias='_'
    )

    dc_id: int
    token: Bytes
