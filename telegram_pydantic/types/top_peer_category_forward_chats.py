from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TopPeerCategoryForwardChats(BaseModel):
    """
    types.TopPeerCategoryForwardChats
    ID: 0xfbeec0f0
    Layer: 181
    """
    QUALNAME: typing.Literal['types.TopPeerCategoryForwardChats', 'TopPeerCategoryForwardChats'] = pydantic.Field(
        'types.TopPeerCategoryForwardChats',
        alias='_'
    )

