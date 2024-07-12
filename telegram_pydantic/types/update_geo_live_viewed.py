from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateGeoLiveViewed(BaseModel):
    """
    types.UpdateGeoLiveViewed
    ID: 0x871fb939
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateGeoLiveViewed', 'UpdateGeoLiveViewed'] = pydantic.Field(
        'types.UpdateGeoLiveViewed',
        alias='_'
    )

    peer: "base.Peer"
    msg_id: int
