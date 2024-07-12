from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PeerSettings(BaseModel):
    """
    types.PeerSettings
    ID: 0xacd66c5e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PeerSettings', 'PeerSettings'] = pydantic.Field(
        'types.PeerSettings',
        alias='_'
    )

    report_spam: typing.Optional[bool] = None
    add_contact: typing.Optional[bool] = None
    block_contact: typing.Optional[bool] = None
    share_contact: typing.Optional[bool] = None
    need_contacts_exception: typing.Optional[bool] = None
    report_geo: typing.Optional[bool] = None
    autoarchived: typing.Optional[bool] = None
    invite_members: typing.Optional[bool] = None
    request_chat_broadcast: typing.Optional[bool] = None
    business_bot_paused: typing.Optional[bool] = None
    business_bot_can_reply: typing.Optional[bool] = None
    geo_distance: typing.Optional[int] = None
    request_chat_title: typing.Optional[str] = None
    request_chat_date: typing.Optional[Datetime] = None
    business_bot_id: typing.Optional[int] = None
    business_bot_manage_url: typing.Optional[str] = None
