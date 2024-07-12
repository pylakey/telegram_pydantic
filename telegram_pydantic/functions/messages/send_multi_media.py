from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendMultiMedia(BaseModel):
    """
    functions.messages.SendMultiMedia
    ID: 0x37b74355
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.SendMultiMedia', 'SendMultiMedia'] = pydantic.Field(
        'functions.messages.SendMultiMedia',
        alias='_'
    )

    peer: "base.InputPeer"
    multi_media: list["base.InputSingleMedia"]
    silent: typing.Optional[bool] = None
    background: typing.Optional[bool] = None
    clear_draft: typing.Optional[bool] = None
    noforwards: typing.Optional[bool] = None
    update_stickersets_order: typing.Optional[bool] = None
    invert_media: typing.Optional[bool] = None
    reply_to: typing.Optional["base.InputReplyTo"] = None
    schedule_date: Datetime
    send_as: typing.Optional["base.InputPeer"] = None
    quick_reply_shortcut: typing.Optional["base.InputQuickReplyShortcut"] = None
    effect: typing.Optional[int] = None
