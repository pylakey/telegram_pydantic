from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GroupCall(BaseModel):
    """
    types.GroupCall
    ID: 0xd597650c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.GroupCall', 'GroupCall'] = pydantic.Field(
        'types.GroupCall',
        alias='_'
    )

    id: int
    access_hash: int
    participants_count: int
    unmuted_video_limit: int
    version: int
    join_muted: typing.Optional[bool] = None
    can_change_join_muted: typing.Optional[bool] = None
    join_date_asc: typing.Optional[bool] = None
    schedule_start_subscribed: typing.Optional[bool] = None
    can_start_video: typing.Optional[bool] = None
    record_video_active: typing.Optional[bool] = None
    rtmp_stream: typing.Optional[bool] = None
    listeners_hidden: typing.Optional[bool] = None
    title: typing.Optional[str] = None
    stream_dc_id: typing.Optional[int] = None
    record_start_date: typing.Optional[Datetime] = None
    schedule_date: typing.Optional[Datetime] = None
    unmuted_video_count: typing.Optional[int] = None
