from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TextSuperscript(BaseModel):
    """
    types.TextSuperscript
    ID: 0xc7fb5e01
    Layer: 181
    """
    QUALNAME: typing.Literal['types.TextSuperscript', 'TextSuperscript'] = pydantic.Field(
        'types.TextSuperscript',
        alias='_'
    )

    text: "base.RichText"
