from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DeletePhoneCallHistory(BaseModel):
    """
    functions.messages.DeletePhoneCallHistory
    ID: 0xf9cbe409
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.DeletePhoneCallHistory', 'DeletePhoneCallHistory'] = pydantic.Field(
        'functions.messages.DeletePhoneCallHistory',
        alias='_'
    )

    revoke: typing.Optional[bool] = None
