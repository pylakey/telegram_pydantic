from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TextConcat(BaseModel):
    """
    types.TextConcat
    ID: 0x7e6260d7
    Layer: 181
    """
    QUALNAME: typing.Literal['types.TextConcat', 'TextConcat'] = pydantic.Field(
        'types.TextConcat',
        alias='_'
    )

    texts: list["base.RichText"]
