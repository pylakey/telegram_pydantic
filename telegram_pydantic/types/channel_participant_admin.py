from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelParticipantAdmin(BaseModel):
    """
    types.ChannelParticipantAdmin
    ID: 0x34c3bb53
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelParticipantAdmin', 'ChannelParticipantAdmin'] = pydantic.Field(
        'types.ChannelParticipantAdmin',
        alias='_'
    )

    user_id: int
    promoted_by: int
    date: Datetime
    admin_rights: "base.ChatAdminRights"
    can_edit: typing.Optional[bool] = None
    is_self: typing.Optional[bool] = pydantic.Field(
        None,
        serialization_alias='self',
        validation_alias=pydantic.AliasChoices('self', 'is_self')
    )
    inviter_id: typing.Optional[int] = None
    rank: typing.Optional[str] = None
