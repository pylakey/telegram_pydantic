from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetCollectibleInfo(BaseModel):
    """
    functions.fragment.GetCollectibleInfo
    ID: 0xbe1e85ba
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.fragment.GetCollectibleInfo', 'GetCollectibleInfo'] = pydantic.Field(
        'functions.fragment.GetCollectibleInfo',
        alias='_'
    )

    collectible: "base.InputCollectible"
