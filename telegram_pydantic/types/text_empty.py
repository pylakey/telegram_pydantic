from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TextEmpty(BaseModel):
    """
    types.TextEmpty
    ID: 0xdc3d824f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.TextEmpty', 'TextEmpty'] = pydantic.Field(
        'types.TextEmpty',
        alias='_'
    )

