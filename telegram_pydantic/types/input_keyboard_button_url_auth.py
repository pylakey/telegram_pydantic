from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputKeyboardButtonUrlAuth(BaseModel):
    """
    types.InputKeyboardButtonUrlAuth
    ID: 0xd02e7fd4
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputKeyboardButtonUrlAuth', 'InputKeyboardButtonUrlAuth'] = pydantic.Field(
        'types.InputKeyboardButtonUrlAuth',
        alias='_'
    )

    text: str
    url: str
    bot: "base.InputUser"
    request_write_access: typing.Optional[bool] = None
    fwd_text: typing.Optional[str] = None
