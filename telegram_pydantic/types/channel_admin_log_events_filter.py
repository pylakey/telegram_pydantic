from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventsFilter(BaseModel):
    """
    types.ChannelAdminLogEventsFilter
    ID: 0xea107ae4
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventsFilter', 'ChannelAdminLogEventsFilter'] = pydantic.Field(
        'types.ChannelAdminLogEventsFilter',
        alias='_'
    )

    join: typing.Optional[bool] = None
    leave: typing.Optional[bool] = None
    invite: typing.Optional[bool] = None
    ban: typing.Optional[bool] = None
    unban: typing.Optional[bool] = None
    kick: typing.Optional[bool] = None
    unkick: typing.Optional[bool] = None
    promote: typing.Optional[bool] = None
    demote: typing.Optional[bool] = None
    info: typing.Optional[bool] = None
    settings: typing.Optional[bool] = None
    pinned: typing.Optional[bool] = None
    edit: typing.Optional[bool] = None
    delete: typing.Optional[bool] = None
    group_call: typing.Optional[bool] = None
    invites: typing.Optional[bool] = None
    send: typing.Optional[bool] = None
    forums: typing.Optional[bool] = None
