from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateBotChatInviteRequester(BaseModel):
    """
    types.UpdateBotChatInviteRequester
    ID: 0x11dfa986
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateBotChatInviteRequester', 'UpdateBotChatInviteRequester'] = pydantic.Field(
        'types.UpdateBotChatInviteRequester',
        alias='_'
    )

    peer: "base.Peer"
    date: Datetime
    user_id: int
    about: str
    invite: "base.ExportedChatInvite"
    qts: int
