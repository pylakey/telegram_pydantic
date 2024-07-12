from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InlineQueryPeerTypeMegagroup(BaseModel):
    """
    types.InlineQueryPeerTypeMegagroup
    ID: 0x5ec4be43
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InlineQueryPeerTypeMegagroup', 'InlineQueryPeerTypeMegagroup'] = pydantic.Field(
        'types.InlineQueryPeerTypeMegagroup',
        alias='_'
    )

