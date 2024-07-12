from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputChatPhotoEmpty(BaseModel):
    """
    types.InputChatPhotoEmpty
    ID: 0x1ca48f57
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputChatPhotoEmpty', 'InputChatPhotoEmpty'] = pydantic.Field(
        'types.InputChatPhotoEmpty',
        alias='_'
    )

