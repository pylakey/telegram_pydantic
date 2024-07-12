from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PeerColor(BaseModel):
    """
    types.PeerColor
    ID: 0xb54b5acf
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PeerColor', 'PeerColor'] = pydantic.Field(
        'types.PeerColor',
        alias='_'
    )

    color: typing.Optional[int] = None
    background_emoji_id: typing.Optional[int] = None
