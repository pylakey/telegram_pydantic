from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TextMarked(BaseModel):
    """
    types.TextMarked
    ID: 0x34b8621
    Layer: 181
    """
    QUALNAME: typing.Literal['types.TextMarked', 'TextMarked'] = pydantic.Field(
        'types.TextMarked',
        alias='_'
    )

    text: "base.RichText"
