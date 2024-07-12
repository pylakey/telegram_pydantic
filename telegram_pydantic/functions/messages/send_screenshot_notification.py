from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendScreenshotNotification(BaseModel):
    """
    functions.messages.SendScreenshotNotification
    ID: 0xa1405817
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.SendScreenshotNotification', 'SendScreenshotNotification'] = pydantic.Field(
        'functions.messages.SendScreenshotNotification',
        alias='_'
    )

    peer: "base.InputPeer"
    reply_to: "base.InputReplyTo"
    random_id: int
