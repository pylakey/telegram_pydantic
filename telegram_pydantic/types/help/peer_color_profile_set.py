from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PeerColorProfileSet(BaseModel):
    """
    types.help.PeerColorProfileSet
    ID: 0x767d61eb
    Layer: 181
    """
    QUALNAME: typing.Literal['types.help.PeerColorProfileSet', 'PeerColorProfileSet'] = pydantic.Field(
        'types.help.PeerColorProfileSet',
        alias='_'
    )

    palette_colors: list[int]
    bg_colors: list[int]
    story_colors: list[int]
