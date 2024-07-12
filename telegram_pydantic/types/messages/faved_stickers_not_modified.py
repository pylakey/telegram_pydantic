from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class FavedStickersNotModified(BaseModel):
    """
    types.messages.FavedStickersNotModified
    ID: 0x9e8fa6d3
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.FavedStickersNotModified', 'FavedStickersNotModified'] = pydantic.Field(
        'types.messages.FavedStickersNotModified',
        alias='_'
    )

