from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GroupCallParticipant(BaseModel):
    """
    types.GroupCallParticipant
    ID: 0xeba636fe
    Layer: 181
    """
    QUALNAME: typing.Literal['types.GroupCallParticipant', 'GroupCallParticipant'] = pydantic.Field(
        'types.GroupCallParticipant',
        alias='_'
    )

    peer: "base.Peer"
    date: Datetime
    source: int
    muted: typing.Optional[bool] = None
    left: typing.Optional[bool] = None
    can_self_unmute: typing.Optional[bool] = None
    just_joined: typing.Optional[bool] = None
    versioned: typing.Optional[bool] = None
    min: typing.Optional[bool] = None
    muted_by_you: typing.Optional[bool] = None
    volume_by_admin: typing.Optional[bool] = None
    is_self: typing.Optional[bool] = pydantic.Field(
        None,
        serialization_alias='self',
        validation_alias=pydantic.AliasChoices('self', 'is_self')
    )
    video_joined: typing.Optional[bool] = None
    active_date: Datetime
    volume: typing.Optional[int] = None
    about: typing.Optional[str] = None
    raise_hand_rating: typing.Optional[int] = None
    video: typing.Optional["base.GroupCallParticipantVideo"] = None
    presentation: typing.Optional["base.GroupCallParticipantVideo"] = None
