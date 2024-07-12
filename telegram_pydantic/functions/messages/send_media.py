from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendMedia(BaseModel):
    """
    functions.messages.SendMedia
    ID: 0x7852834e
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.SendMedia', 'SendMedia'] = pydantic.Field(
        'functions.messages.SendMedia',
        alias='_'
    )

    peer: "base.InputPeer"
    media: "base.InputMedia"
    message: str
    random_id: int
    silent: typing.Optional[bool] = None
    background: typing.Optional[bool] = None
    clear_draft: typing.Optional[bool] = None
    noforwards: typing.Optional[bool] = None
    update_stickersets_order: typing.Optional[bool] = None
    invert_media: typing.Optional[bool] = None
    reply_to: typing.Optional["base.InputReplyTo"] = None
    reply_markup: typing.Optional["base.ReplyMarkup"] = None
    entities: typing.Optional[list["base.MessageEntity"]] = None
    schedule_date: typing.Optional[Datetime] = None
    send_as: typing.Optional["base.InputPeer"] = None
    quick_reply_shortcut: typing.Optional["base.InputQuickReplyShortcut"] = None
    effect: typing.Optional[int] = None
