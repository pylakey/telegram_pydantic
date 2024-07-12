from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TextFixed(BaseModel):
    """
    types.TextFixed
    ID: 0x6c3f19b9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.TextFixed', 'TextFixed'] = pydantic.Field(
        'types.TextFixed',
        alias='_'
    )

    text: "base.RichText"
