from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionChangeTitle(BaseModel):
    """
    types.ChannelAdminLogEventActionChangeTitle
    ID: 0xe6dfb825
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionChangeTitle', 'ChannelAdminLogEventActionChangeTitle'] = pydantic.Field(
        'types.ChannelAdminLogEventActionChangeTitle',
        alias='_'
    )

    prev_value: str
    new_value: str
