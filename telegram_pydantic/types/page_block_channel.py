from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageBlockChannel(BaseModel):
    """
    types.PageBlockChannel
    ID: 0xef1751b5
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageBlockChannel', 'PageBlockChannel'] = pydantic.Field(
        'types.PageBlockChannel',
        alias='_'
    )

    channel: "base.Chat"
