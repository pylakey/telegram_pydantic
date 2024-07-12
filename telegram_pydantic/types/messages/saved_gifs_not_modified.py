from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SavedGifsNotModified(BaseModel):
    """
    types.messages.SavedGifsNotModified
    ID: 0xe8025ca2
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.SavedGifsNotModified', 'SavedGifsNotModified'] = pydantic.Field(
        'types.messages.SavedGifsNotModified',
        alias='_'
    )

