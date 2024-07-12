from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateMessageExtendedMedia(BaseModel):
    """
    types.UpdateMessageExtendedMedia
    ID: 0x5a73a98c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateMessageExtendedMedia', 'UpdateMessageExtendedMedia'] = pydantic.Field(
        'types.UpdateMessageExtendedMedia',
        alias='_'
    )

    peer: "base.Peer"
    msg_id: int
    extended_media: "base.MessageExtendedMedia"
