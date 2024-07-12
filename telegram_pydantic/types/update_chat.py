from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateChat(BaseModel):
    """
    types.UpdateChat
    ID: 0xf89a6a4e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateChat', 'UpdateChat'] = pydantic.Field(
        'types.UpdateChat',
        alias='_'
    )

    chat_id: int
