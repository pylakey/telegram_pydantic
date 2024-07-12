from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DeleteQuickReplyShortcut(BaseModel):
    """
    functions.messages.DeleteQuickReplyShortcut
    ID: 0x3cc04740
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.DeleteQuickReplyShortcut', 'DeleteQuickReplyShortcut'] = pydantic.Field(
        'functions.messages.DeleteQuickReplyShortcut',
        alias='_'
    )

    shortcut_id: int
