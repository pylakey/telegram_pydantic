from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DifferenceTooLong(BaseModel):
    """
    types.updates.DifferenceTooLong
    ID: 0x4afe8f6d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.updates.DifferenceTooLong', 'DifferenceTooLong'] = pydantic.Field(
        'types.updates.DifferenceTooLong',
        alias='_'
    )

    pts: int
