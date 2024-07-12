from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TopPeerCategoryBotsPM(BaseModel):
    """
    types.TopPeerCategoryBotsPM
    ID: 0xab661b5b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.TopPeerCategoryBotsPM', 'TopPeerCategoryBotsPM'] = pydantic.Field(
        'types.TopPeerCategoryBotsPM',
        alias='_'
    )

