from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionChangePhoto(BaseModel):
    """
    types.ChannelAdminLogEventActionChangePhoto
    ID: 0x434bd2af
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionChangePhoto', 'ChannelAdminLogEventActionChangePhoto'] = pydantic.Field(
        'types.ChannelAdminLogEventActionChangePhoto',
        alias='_'
    )

    prev_photo: "base.Photo"
    new_photo: "base.Photo"
