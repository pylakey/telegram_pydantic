from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetInlineBotResults(BaseModel):
    """
    functions.messages.GetInlineBotResults
    ID: 0x514e999d
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetInlineBotResults', 'GetInlineBotResults'] = pydantic.Field(
        'functions.messages.GetInlineBotResults',
        alias='_'
    )

    bot: "base.InputUser"
    peer: "base.InputPeer"
    query: str
    offset: str
    geo_point: typing.Optional["base.InputGeoPoint"] = None
