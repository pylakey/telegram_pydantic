from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateReadHistoryOutbox(BaseModel):
    """
    types.UpdateReadHistoryOutbox
    ID: 0x2f2f21bf
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateReadHistoryOutbox', 'UpdateReadHistoryOutbox'] = pydantic.Field(
        'types.UpdateReadHistoryOutbox',
        alias='_'
    )

    peer: "base.Peer"
    max_id: int
    pts: int
    pts_count: int
