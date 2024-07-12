from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateReadHistoryInbox(BaseModel):
    """
    types.UpdateReadHistoryInbox
    ID: 0x9c974fdf
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateReadHistoryInbox', 'UpdateReadHistoryInbox'] = pydantic.Field(
        'types.UpdateReadHistoryInbox',
        alias='_'
    )

    peer: "base.Peer"
    max_id: int
    still_unread_count: int
    pts: int
    pts_count: int
    folder_id: typing.Optional[int] = None
