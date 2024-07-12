from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TextPhone(BaseModel):
    """
    types.TextPhone
    ID: 0x1ccb966a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.TextPhone', 'TextPhone'] = pydantic.Field(
        'types.TextPhone',
        alias='_'
    )

    text: "base.RichText"
    phone: str
