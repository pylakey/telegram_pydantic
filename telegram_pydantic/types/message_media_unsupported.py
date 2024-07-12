from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageMediaUnsupported(BaseModel):
    """
    types.MessageMediaUnsupported
    ID: 0x9f84f49e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageMediaUnsupported', 'MessageMediaUnsupported'] = pydantic.Field(
        'types.MessageMediaUnsupported',
        alias='_'
    )

