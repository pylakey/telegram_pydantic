from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DocumentEmpty(BaseModel):
    """
    types.DocumentEmpty
    ID: 0x36f8c871
    Layer: 181
    """
    QUALNAME: typing.Literal['types.DocumentEmpty', 'DocumentEmpty'] = pydantic.Field(
        'types.DocumentEmpty',
        alias='_'
    )

    id: int
