from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ViewSponsoredMessage(BaseModel):
    """
    functions.channels.ViewSponsoredMessage
    ID: 0xbeaedb94
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.ViewSponsoredMessage', 'ViewSponsoredMessage'] = pydantic.Field(
        'functions.channels.ViewSponsoredMessage',
        alias='_'
    )

    channel: "base.InputChannel"
    random_id: Bytes
