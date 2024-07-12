from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PublicForwardMessage(BaseModel):
    """
    types.PublicForwardMessage
    ID: 0x1f2bf4a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PublicForwardMessage', 'PublicForwardMessage'] = pydantic.Field(
        'types.PublicForwardMessage',
        alias='_'
    )

    message: "base.Message"
