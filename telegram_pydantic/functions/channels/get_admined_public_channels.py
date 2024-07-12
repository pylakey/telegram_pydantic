from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetAdminedPublicChannels(BaseModel):
    """
    functions.channels.GetAdminedPublicChannels
    ID: 0xf8b036af
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.GetAdminedPublicChannels', 'GetAdminedPublicChannels'] = pydantic.Field(
        'functions.channels.GetAdminedPublicChannels',
        alias='_'
    )

    by_location: typing.Optional[bool] = None
    check_limit: typing.Optional[bool] = None
    for_personal: typing.Optional[bool] = None
