from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Dialog(BaseModel):
    """
    types.Dialog
    ID: 0xd58a08c6
    Layer: 181
    """
    QUALNAME: typing.Literal['types.Dialog', 'Dialog'] = pydantic.Field(
        'types.Dialog',
        alias='_'
    )

    peer: "base.Peer"
    top_message: int
    read_inbox_max_id: int
    read_outbox_max_id: int
    unread_count: int
    unread_mentions_count: int
    unread_reactions_count: int
    notify_settings: "base.PeerNotifySettings"
    pinned: typing.Optional[bool] = None
    unread_mark: typing.Optional[bool] = None
    view_forum_as_messages: typing.Optional[bool] = None
    pts: typing.Optional[int] = None
    draft: typing.Optional["base.DraftMessage"] = None
    folder_id: typing.Optional[int] = None
    ttl_period: typing.Optional[int] = None
