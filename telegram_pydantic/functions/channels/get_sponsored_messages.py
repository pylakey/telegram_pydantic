from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetSponsoredMessages(BaseModel):
    """
    functions.channels.GetSponsoredMessages
    ID: 0xec210fbf
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.GetSponsoredMessages', 'GetSponsoredMessages'] = pydantic.Field(
        'functions.channels.GetSponsoredMessages',
        alias='_'
    )

    channel: "base.InputChannel"
