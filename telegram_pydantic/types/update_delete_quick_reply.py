from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateDeleteQuickReply(BaseModel):
    """
    types.UpdateDeleteQuickReply
    ID: 0x53e6f1ec
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateDeleteQuickReply', 'UpdateDeleteQuickReply'] = pydantic.Field(
        'types.UpdateDeleteQuickReply',
        alias='_'
    )

    shortcut_id: int
