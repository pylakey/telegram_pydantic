from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateReadChannelOutbox(BaseModel):
    """
    types.UpdateReadChannelOutbox
    ID: 0xb75f99a9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateReadChannelOutbox', 'UpdateReadChannelOutbox'] = pydantic.Field(
        'types.UpdateReadChannelOutbox',
        alias='_'
    )

    channel_id: int
    max_id: int
