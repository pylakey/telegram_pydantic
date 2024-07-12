from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SaveDefaultGroupCallJoinAs(BaseModel):
    """
    functions.phone.SaveDefaultGroupCallJoinAs
    ID: 0x575e1f8c
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.phone.SaveDefaultGroupCallJoinAs', 'SaveDefaultGroupCallJoinAs'] = pydantic.Field(
        'functions.phone.SaveDefaultGroupCallJoinAs',
        alias='_'
    )

    peer: "base.InputPeer"
    join_as: "base.InputPeer"
