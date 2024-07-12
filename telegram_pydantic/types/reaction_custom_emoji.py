from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReactionCustomEmoji(BaseModel):
    """
    types.ReactionCustomEmoji
    ID: 0x8935fc73
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ReactionCustomEmoji', 'ReactionCustomEmoji'] = pydantic.Field(
        'types.ReactionCustomEmoji',
        alias='_'
    )

    document_id: int
