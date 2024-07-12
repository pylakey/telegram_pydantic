from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateColor(BaseModel):
    """
    functions.account.UpdateColor
    ID: 0x7cefa15d
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.UpdateColor', 'UpdateColor'] = pydantic.Field(
        'functions.account.UpdateColor',
        alias='_'
    )

    for_profile: typing.Optional[bool] = None
    color: typing.Optional[int] = None
    background_emoji_id: typing.Optional[int] = None
