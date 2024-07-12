from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendMessage(BaseModel):
    """
    functions.messages.SendMessage
    ID: 0x983f9745
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.SendMessage', 'SendMessage'] = pydantic.Field(
        'functions.messages.SendMessage',
        alias='_'
    )

    peer: "base.InputPeer"
    message: str
    random_id: int
    no_webpage: typing.Optional[bool] = None
    silent: typing.Optional[bool] = None
    background: typing.Optional[bool] = None
    clear_draft: typing.Optional[bool] = None
    noforwards: typing.Optional[bool] = None
    update_stickersets_order: typing.Optional[bool] = None
    invert_media: typing.Optional[bool] = None
    reply_to: typing.Optional["base.InputReplyTo"] = None
    reply_markup: typing.Optional["base.ReplyMarkup"] = None
    entities: typing.Optional[list["base.MessageEntity"]] = None
    schedule_date: Datetime
    send_as: typing.Optional["base.InputPeer"] = None
    quick_reply_shortcut: typing.Optional["base.InputQuickReplyShortcut"] = None
    effect: typing.Optional[int] = None
