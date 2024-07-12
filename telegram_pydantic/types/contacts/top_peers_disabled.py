from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TopPeersDisabled(BaseModel):
    """
    types.contacts.TopPeersDisabled
    ID: 0xb52c939d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.contacts.TopPeersDisabled', 'TopPeersDisabled'] = pydantic.Field(
        'types.contacts.TopPeersDisabled',
        alias='_'
    )

