from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateNewEncryptedMessage(BaseModel):
    """
    types.UpdateNewEncryptedMessage
    ID: 0x12bcbd9a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateNewEncryptedMessage', 'UpdateNewEncryptedMessage'] = pydantic.Field(
        'types.UpdateNewEncryptedMessage',
        alias='_'
    )

    message: "base.EncryptedMessage"
    qts: int
