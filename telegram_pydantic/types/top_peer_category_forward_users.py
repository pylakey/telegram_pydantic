from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TopPeerCategoryForwardUsers(BaseModel):
    """
    types.TopPeerCategoryForwardUsers
    ID: 0xa8406ca9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.TopPeerCategoryForwardUsers', 'TopPeerCategoryForwardUsers'] = pydantic.Field(
        'types.TopPeerCategoryForwardUsers',
        alias='_'
    )

