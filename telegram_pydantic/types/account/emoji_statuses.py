from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EmojiStatuses(BaseModel):
    """
    types.account.EmojiStatuses
    ID: 0x90c467d1
    Layer: 181
    """
    QUALNAME: typing.Literal['types.account.EmojiStatuses', 'EmojiStatuses'] = pydantic.Field(
        'types.account.EmojiStatuses',
        alias='_'
    )

    hash: int
    statuses: list["base.EmojiStatus"]
