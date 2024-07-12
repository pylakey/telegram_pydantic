from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CheckedHistoryImportPeer(BaseModel):
    """
    types.messages.CheckedHistoryImportPeer
    ID: 0xa24de717
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.CheckedHistoryImportPeer', 'CheckedHistoryImportPeer'] = pydantic.Field(
        'types.messages.CheckedHistoryImportPeer',
        alias='_'
    )

    confirm_text: str
