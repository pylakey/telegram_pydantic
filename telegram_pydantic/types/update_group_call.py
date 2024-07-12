from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateGroupCall(BaseModel):
    """
    types.UpdateGroupCall
    ID: 0x14b24500
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateGroupCall', 'UpdateGroupCall'] = pydantic.Field(
        'types.UpdateGroupCall',
        alias='_'
    )

    chat_id: int
    call: "base.GroupCall"
