from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetExtendedMedia(BaseModel):
    """
    functions.messages.GetExtendedMedia
    ID: 0x84f80814
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetExtendedMedia', 'GetExtendedMedia'] = pydantic.Field(
        'functions.messages.GetExtendedMedia',
        alias='_'
    )

    peer: "base.InputPeer"
    id: list[int]
