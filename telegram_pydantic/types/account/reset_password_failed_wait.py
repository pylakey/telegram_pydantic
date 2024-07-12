from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ResetPasswordFailedWait(BaseModel):
    """
    types.account.ResetPasswordFailedWait
    ID: 0xe3779861
    Layer: 181
    """
    QUALNAME: typing.Literal['types.account.ResetPasswordFailedWait', 'ResetPasswordFailedWait'] = pydantic.Field(
        'types.account.ResetPasswordFailedWait',
        alias='_'
    )

    retry_date: Datetime
