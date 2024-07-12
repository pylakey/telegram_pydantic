from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetUserBoosts(BaseModel):
    """
    functions.premium.GetUserBoosts
    ID: 0x39854d1f
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.premium.GetUserBoosts', 'GetUserBoosts'] = pydantic.Field(
        'functions.premium.GetUserBoosts',
        alias='_'
    )

    peer: "base.InputPeer"
    user_id: "base.InputUser"
