from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GroupCallParticipantVideo(BaseModel):
    """
    types.GroupCallParticipantVideo
    ID: 0x67753ac8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.GroupCallParticipantVideo', 'GroupCallParticipantVideo'] = pydantic.Field(
        'types.GroupCallParticipantVideo',
        alias='_'
    )

    endpoint: str
    source_groups: list["base.GroupCallParticipantVideoSourceGroup"]
    paused: typing.Optional[bool] = None
    audio_source: typing.Optional[int] = None
