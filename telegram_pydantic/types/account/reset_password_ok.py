from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ResetPasswordOk(BaseModel):
    """
    types.account.ResetPasswordOk
    ID: 0xe926d63e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.account.ResetPasswordOk', 'ResetPasswordOk'] = pydantic.Field(
        'types.account.ResetPasswordOk',
        alias='_'
    )

