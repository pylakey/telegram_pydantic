from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetGroupCallJoinAs(BaseModel):
    """
    functions.phone.GetGroupCallJoinAs
    ID: 0xef7c213a
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.phone.GetGroupCallJoinAs', 'GetGroupCallJoinAs'] = pydantic.Field(
        'functions.phone.GetGroupCallJoinAs',
        alias='_'
    )

    peer: "base.InputPeer"
