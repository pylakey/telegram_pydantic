from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SetBoostsToUnblockRestrictions(BaseModel):
    """
    functions.channels.SetBoostsToUnblockRestrictions
    ID: 0xad399cee
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.SetBoostsToUnblockRestrictions', 'SetBoostsToUnblockRestrictions'] = pydantic.Field(
        'functions.channels.SetBoostsToUnblockRestrictions',
        alias='_'
    )

    channel: "base.InputChannel"
    boosts: int
