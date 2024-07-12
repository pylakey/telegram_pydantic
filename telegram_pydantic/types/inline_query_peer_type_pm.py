from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InlineQueryPeerTypePM(BaseModel):
    """
    types.InlineQueryPeerTypePM
    ID: 0x833c0fac
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InlineQueryPeerTypePM', 'InlineQueryPeerTypePM'] = pydantic.Field(
        'types.InlineQueryPeerTypePM',
        alias='_'
    )

