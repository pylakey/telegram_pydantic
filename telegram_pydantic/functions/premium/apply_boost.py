from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ApplyBoost(BaseModel):
    """
    functions.premium.ApplyBoost
    ID: 0x6b7da746
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.premium.ApplyBoost', 'ApplyBoost'] = pydantic.Field(
        'functions.premium.ApplyBoost',
        alias='_'
    )

    peer: "base.InputPeer"
    slots: typing.Optional[list[int]] = None
