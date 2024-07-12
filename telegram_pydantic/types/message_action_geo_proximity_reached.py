from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionGeoProximityReached(BaseModel):
    """
    types.MessageActionGeoProximityReached
    ID: 0x98e0d697
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionGeoProximityReached', 'MessageActionGeoProximityReached'] = pydantic.Field(
        'types.MessageActionGeoProximityReached',
        alias='_'
    )

    from_id: "base.Peer"
    to_id: "base.Peer"
    distance: int
