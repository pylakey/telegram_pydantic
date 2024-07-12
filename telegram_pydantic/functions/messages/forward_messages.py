from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ForwardMessages(BaseModel):
    """
    functions.messages.ForwardMessages
    ID: 0xd5039208
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.ForwardMessages', 'ForwardMessages'] = pydantic.Field(
        'functions.messages.ForwardMessages',
        alias='_'
    )

    from_peer: "base.InputPeer"
    id: list[int]
    random_id: list[int]
    to_peer: "base.InputPeer"
    silent: typing.Optional[bool] = None
    background: typing.Optional[bool] = None
    with_my_score: typing.Optional[bool] = None
    drop_author: typing.Optional[bool] = None
    drop_media_captions: typing.Optional[bool] = None
    noforwards: typing.Optional[bool] = None
    top_msg_id: typing.Optional[int] = None
    schedule_date: Datetime
    send_as: typing.Optional["base.InputPeer"] = None
    quick_reply_shortcut: typing.Optional["base.InputQuickReplyShortcut"] = None
