from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetMyBoosts(BaseModel):
    """
    functions.premium.GetMyBoosts
    ID: 0xbe77b4a
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.premium.GetMyBoosts', 'GetMyBoosts'] = pydantic.Field(
        'functions.premium.GetMyBoosts',
        alias='_'
    )

