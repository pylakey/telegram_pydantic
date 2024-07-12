from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendMessageUploadVideoAction(BaseModel):
    """
    types.SendMessageUploadVideoAction
    ID: 0xe9763aec
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SendMessageUploadVideoAction', 'SendMessageUploadVideoAction'] = pydantic.Field(
        'types.SendMessageUploadVideoAction',
        alias='_'
    )

    progress: int
