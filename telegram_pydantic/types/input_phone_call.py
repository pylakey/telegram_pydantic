from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPhoneCall(BaseModel):
    """
    types.InputPhoneCall
    ID: 0x1e36fded
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPhoneCall', 'InputPhoneCall'] = pydantic.Field(
        'types.InputPhoneCall',
        alias='_'
    )

    id: int
    access_hash: int
