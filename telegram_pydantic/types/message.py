from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Message(BaseModel):
    """
    types.Message
    ID: 0x94345242
    Layer: 181
    """
    QUALNAME: typing.Literal['types.Message', 'Message'] = pydantic.Field(
        'types.Message',
        alias='_'
    )

    id: int
    peer_id: "base.Peer"
    date: Datetime
    message: str
    out: typing.Optional[bool] = None
    mentioned: typing.Optional[bool] = None
    media_unread: typing.Optional[bool] = None
    silent: typing.Optional[bool] = None
    post: typing.Optional[bool] = None
    from_scheduled: typing.Optional[bool] = None
    legacy: typing.Optional[bool] = None
    edit_hide: typing.Optional[bool] = None
    pinned: typing.Optional[bool] = None
    noforwards: typing.Optional[bool] = None
    invert_media: typing.Optional[bool] = None
    offline: typing.Optional[bool] = None
    from_id: typing.Optional["base.Peer"] = None
    from_boosts_applied: typing.Optional[int] = None
    saved_peer_id: typing.Optional["base.Peer"] = None
    fwd_from: typing.Optional["base.MessageFwdHeader"] = None
    via_bot_id: typing.Optional[int] = None
    via_business_bot_id: typing.Optional[int] = None
    reply_to: typing.Optional["base.MessageReplyHeader"] = None
    media: typing.Optional["base.MessageMedia"] = None
    reply_markup: typing.Optional["base.ReplyMarkup"] = None
    entities: typing.Optional[list["base.MessageEntity"]] = None
    views: typing.Optional[int] = None
    forwards: typing.Optional[int] = None
    replies: typing.Optional["base.MessageReplies"] = None
    edit_date: typing.Optional[Datetime] = None
    post_author: typing.Optional[str] = None
    grouped_id: typing.Optional[int] = None
    reactions: typing.Optional["base.MessageReactions"] = None
    restriction_reason: typing.Optional[list["base.RestrictionReason"]] = None
    ttl_period: typing.Optional[int] = None
    quick_reply_shortcut_id: typing.Optional[int] = None
    effect: typing.Optional[int] = None
    factcheck: typing.Optional["base.FactCheck"] = None
