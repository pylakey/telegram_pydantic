from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EncryptedChatDiscarded(BaseModel):
    """
    types.EncryptedChatDiscarded
    ID: 0x1e1c7c45
    Layer: 181
    """
    QUALNAME: typing.Literal['types.EncryptedChatDiscarded', 'EncryptedChatDiscarded'] = pydantic.Field(
        'types.EncryptedChatDiscarded',
        alias='_'
    )

    id: int
    history_deleted: typing.Optional[bool] = None
