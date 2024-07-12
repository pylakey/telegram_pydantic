from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AttachMenuPeerTypeChat(BaseModel):
    """
    types.AttachMenuPeerTypeChat
    ID: 0x509113f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.AttachMenuPeerTypeChat', 'AttachMenuPeerTypeChat'] = pydantic.Field(
        'types.AttachMenuPeerTypeChat',
        alias='_'
    )

