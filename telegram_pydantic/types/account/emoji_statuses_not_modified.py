from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EmojiStatusesNotModified(BaseModel):
    """
    types.account.EmojiStatusesNotModified
    ID: 0xd08ce645
    Layer: 181
    """
    QUALNAME: typing.Literal['types.account.EmojiStatusesNotModified', 'EmojiStatusesNotModified'] = pydantic.Field(
        'types.account.EmojiStatusesNotModified',
        alias='_'
    )

