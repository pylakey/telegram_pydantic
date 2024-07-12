from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetAdminsWithInvites(BaseModel):
    """
    functions.messages.GetAdminsWithInvites
    ID: 0x3920e6ef
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetAdminsWithInvites', 'GetAdminsWithInvites'] = pydantic.Field(
        'functions.messages.GetAdminsWithInvites',
        alias='_'
    )

    peer: "base.InputPeer"
