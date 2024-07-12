from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionInviteToGroupCall(BaseModel):
    """
    types.MessageActionInviteToGroupCall
    ID: 0x502f92f7
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionInviteToGroupCall', 'MessageActionInviteToGroupCall'] = pydantic.Field(
        'types.MessageActionInviteToGroupCall',
        alias='_'
    )

    call: "base.InputGroupCall"
    users: list[int]
