from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Channel(BaseModel):
    """
    types.Channel
    ID: 0xaadfc8f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.Channel', 'Channel'] = pydantic.Field(
        'types.Channel',
        alias='_'
    )

    id: int
    title: str
    photo: "base.ChatPhoto"
    date: Datetime
    creator: typing.Optional[bool] = None
    left: typing.Optional[bool] = None
    broadcast: typing.Optional[bool] = None
    verified: typing.Optional[bool] = None
    megagroup: typing.Optional[bool] = None
    restricted: typing.Optional[bool] = None
    signatures: typing.Optional[bool] = None
    min: typing.Optional[bool] = None
    scam: typing.Optional[bool] = None
    has_link: typing.Optional[bool] = None
    has_geo: typing.Optional[bool] = None
    slowmode_enabled: typing.Optional[bool] = None
    call_active: typing.Optional[bool] = None
    call_not_empty: typing.Optional[bool] = None
    fake: typing.Optional[bool] = None
    gigagroup: typing.Optional[bool] = None
    noforwards: typing.Optional[bool] = None
    join_to_send: typing.Optional[bool] = None
    join_request: typing.Optional[bool] = None
    forum: typing.Optional[bool] = None
    stories_hidden: typing.Optional[bool] = None
    stories_hidden_min: typing.Optional[bool] = None
    stories_unavailable: typing.Optional[bool] = None
    access_hash: typing.Optional[int] = None
    username: typing.Optional[str] = None
    restriction_reason: typing.Optional[list["base.RestrictionReason"]] = None
    admin_rights: typing.Optional["base.ChatAdminRights"] = None
    banned_rights: typing.Optional["base.ChatBannedRights"] = None
    default_banned_rights: typing.Optional["base.ChatBannedRights"] = None
    participants_count: typing.Optional[int] = None
    usernames: typing.Optional[list["base.Username"]] = None
    stories_max_id: typing.Optional[int] = None
    color: typing.Optional["base.PeerColor"] = None
    profile_color: typing.Optional["base.PeerColor"] = None
    emoji_status: typing.Optional["base.EmojiStatus"] = None
    level: typing.Optional[int] = None
