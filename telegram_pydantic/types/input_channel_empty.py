from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputChannelEmpty(BaseModel):
    """
    types.InputChannelEmpty
    ID: 0xee8c1e86
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputChannelEmpty', 'InputChannelEmpty'] = pydantic.Field(
        'types.InputChannelEmpty',
        alias='_'
    )

