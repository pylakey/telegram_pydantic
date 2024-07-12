from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionEmpty(BaseModel):
    """
    types.MessageActionEmpty
    ID: 0xb6aef7b0
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionEmpty', 'MessageActionEmpty'] = pydantic.Field(
        'types.MessageActionEmpty',
        alias='_'
    )

