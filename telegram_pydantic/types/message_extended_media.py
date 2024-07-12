from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageExtendedMedia(BaseModel):
    """
    types.MessageExtendedMedia
    ID: 0xee479c64
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageExtendedMedia', 'MessageExtendedMedia'] = pydantic.Field(
        'types.MessageExtendedMedia',
        alias='_'
    )

    media: "base.MessageMedia"
