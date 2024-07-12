from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SavedRingtonesNotModified(BaseModel):
    """
    types.account.SavedRingtonesNotModified
    ID: 0xfbf6e8b1
    Layer: 181
    """
    QUALNAME: typing.Literal['types.account.SavedRingtonesNotModified', 'SavedRingtonesNotModified'] = pydantic.Field(
        'types.account.SavedRingtonesNotModified',
        alias='_'
    )

