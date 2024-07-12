from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SavedDialogsNotModified(BaseModel):
    """
    types.messages.SavedDialogsNotModified
    ID: 0xc01f6fe8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.SavedDialogsNotModified', 'SavedDialogsNotModified'] = pydantic.Field(
        'types.messages.SavedDialogsNotModified',
        alias='_'
    )

    count: int
