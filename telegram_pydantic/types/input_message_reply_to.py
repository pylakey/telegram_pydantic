from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMessageReplyTo(BaseModel):
    """
    types.InputMessageReplyTo
    ID: 0xbad88395
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMessageReplyTo', 'InputMessageReplyTo'] = pydantic.Field(
        'types.InputMessageReplyTo',
        alias='_'
    )

    id: int
