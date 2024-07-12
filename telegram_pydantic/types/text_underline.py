from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TextUnderline(BaseModel):
    """
    types.TextUnderline
    ID: 0xc12622c4
    Layer: 181
    """
    QUALNAME: typing.Literal['types.TextUnderline', 'TextUnderline'] = pydantic.Field(
        'types.TextUnderline',
        alias='_'
    )

    text: "base.RichText"
