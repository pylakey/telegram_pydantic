from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class RequestPasswordRecovery(BaseModel):
    """
    functions.auth.RequestPasswordRecovery
    ID: 0xd897bc66
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.auth.RequestPasswordRecovery', 'RequestPasswordRecovery'] = pydantic.Field(
        'functions.auth.RequestPasswordRecovery',
        alias='_'
    )

