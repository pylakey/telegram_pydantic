from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionGroupCall(BaseModel):
    """
    types.MessageActionGroupCall
    ID: 0x7a0d7f42
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionGroupCall', 'MessageActionGroupCall'] = pydantic.Field(
        'types.MessageActionGroupCall',
        alias='_'
    )

    call: "base.InputGroupCall"
    duration: typing.Optional[int] = None
