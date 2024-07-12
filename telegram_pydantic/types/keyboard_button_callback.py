from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class KeyboardButtonCallback(BaseModel):
    """
    types.KeyboardButtonCallback
    ID: 0x35bbdb6b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.KeyboardButtonCallback', 'KeyboardButtonCallback'] = pydantic.Field(
        'types.KeyboardButtonCallback',
        alias='_'
    )

    text: str
    data: Bytes
    requires_password: typing.Optional[bool] = None
