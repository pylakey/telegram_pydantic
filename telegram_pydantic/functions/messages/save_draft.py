from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SaveDraft(BaseModel):
    """
    functions.messages.SaveDraft
    ID: 0x7ff3b806
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.SaveDraft', 'SaveDraft'] = pydantic.Field(
        'functions.messages.SaveDraft',
        alias='_'
    )

    peer: "base.InputPeer"
    message: str
    no_webpage: typing.Optional[bool] = None
    invert_media: typing.Optional[bool] = None
    reply_to: typing.Optional["base.InputReplyTo"] = None
    entities: typing.Optional[list["base.MessageEntity"]] = None
    media: typing.Optional["base.InputMedia"] = None
