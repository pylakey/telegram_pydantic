from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EditMessage(BaseModel):
    """
    functions.messages.EditMessage
    ID: 0xdfd14005
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.EditMessage', 'EditMessage'] = pydantic.Field(
        'functions.messages.EditMessage',
        alias='_'
    )

    peer: "base.InputPeer"
    id: int
    no_webpage: typing.Optional[bool] = None
    invert_media: typing.Optional[bool] = None
    message: typing.Optional[str] = None
    media: typing.Optional["base.InputMedia"] = None
    reply_markup: typing.Optional["base.ReplyMarkup"] = None
    entities: typing.Optional[list["base.MessageEntity"]] = None
    schedule_date: typing.Optional[Datetime] = None
    quick_reply_shortcut_id: typing.Optional[int] = None
