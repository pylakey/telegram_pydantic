from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InviteToGroupCall(BaseModel):
    """
    functions.phone.InviteToGroupCall
    ID: 0x7b393160
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.phone.InviteToGroupCall', 'InviteToGroupCall'] = pydantic.Field(
        'functions.phone.InviteToGroupCall',
        alias='_'
    )

    call: "base.InputGroupCall"
    users: list["base.InputUser"]
