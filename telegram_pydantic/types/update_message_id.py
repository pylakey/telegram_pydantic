from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateMessageID(BaseModel):
    """
    types.UpdateMessageID
    ID: 0x4e90bfd6
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateMessageID', 'UpdateMessageID'] = pydantic.Field(
        'types.UpdateMessageID',
        alias='_'
    )

    id: int
    random_id: int
