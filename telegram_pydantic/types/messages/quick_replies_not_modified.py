from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class QuickRepliesNotModified(BaseModel):
    """
    types.messages.QuickRepliesNotModified
    ID: 0x5f91eb5b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.QuickRepliesNotModified', 'QuickRepliesNotModified'] = pydantic.Field(
        'types.messages.QuickRepliesNotModified',
        alias='_'
    )

