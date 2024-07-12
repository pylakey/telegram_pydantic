from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetChannelRecommendations(BaseModel):
    """
    functions.channels.GetChannelRecommendations
    ID: 0x25a71742
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.GetChannelRecommendations', 'GetChannelRecommendations'] = pydantic.Field(
        'functions.channels.GetChannelRecommendations',
        alias='_'
    )

    channel: typing.Optional["base.InputChannel"] = None
