from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelMessagesFilter(BaseModel):
    """
    types.ChannelMessagesFilter
    ID: 0xcd77d957
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelMessagesFilter', 'ChannelMessagesFilter'] = pydantic.Field(
        'types.ChannelMessagesFilter',
        alias='_'
    )

    ranges: list["base.MessageRange"]
    exclude_new_messages: typing.Optional[bool] = None
