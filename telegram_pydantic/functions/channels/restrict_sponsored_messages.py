from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class RestrictSponsoredMessages(BaseModel):
    """
    functions.channels.RestrictSponsoredMessages
    ID: 0x9ae91519
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.RestrictSponsoredMessages', 'RestrictSponsoredMessages'] = pydantic.Field(
        'functions.channels.RestrictSponsoredMessages',
        alias='_'
    )

    channel: "base.InputChannel"
    restricted: bool
