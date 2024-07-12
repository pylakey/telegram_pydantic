from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PeerColorSet(BaseModel):
    """
    types.help.PeerColorSet
    ID: 0x26219a58
    Layer: 181
    """
    QUALNAME: typing.Literal['types.help.PeerColorSet', 'PeerColorSet'] = pydantic.Field(
        'types.help.PeerColorSet',
        alias='_'
    )

    colors: list[int]
