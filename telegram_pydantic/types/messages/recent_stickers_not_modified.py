from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class RecentStickersNotModified(BaseModel):
    """
    types.messages.RecentStickersNotModified
    ID: 0xb17f890
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.RecentStickersNotModified', 'RecentStickersNotModified'] = pydantic.Field(
        'types.messages.RecentStickersNotModified',
        alias='_'
    )

