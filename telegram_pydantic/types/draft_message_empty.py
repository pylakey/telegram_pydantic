from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DraftMessageEmpty(BaseModel):
    """
    types.DraftMessageEmpty
    ID: 0x1b0c841a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.DraftMessageEmpty', 'DraftMessageEmpty'] = pydantic.Field(
        'types.DraftMessageEmpty',
        alias='_'
    )

    date: Datetime
