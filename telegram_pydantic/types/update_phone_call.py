from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdatePhoneCall(BaseModel):
    """
    types.UpdatePhoneCall
    ID: 0xab0f6b1e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdatePhoneCall', 'UpdatePhoneCall'] = pydantic.Field(
        'types.UpdatePhoneCall',
        alias='_'
    )

    phone_call: "base.PhoneCall"
