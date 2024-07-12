from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ResetPasswordRequestedWait(BaseModel):
    """
    types.account.ResetPasswordRequestedWait
    ID: 0xe9effc7d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.account.ResetPasswordRequestedWait', 'ResetPasswordRequestedWait'] = pydantic.Field(
        'types.account.ResetPasswordRequestedWait',
        alias='_'
    )

    until_date: Datetime
