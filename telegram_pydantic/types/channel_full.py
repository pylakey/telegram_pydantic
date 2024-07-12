from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelFull(BaseModel):
    """
    types.ChannelFull
    ID: 0xbbab348d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelFull', 'ChannelFull'] = pydantic.Field(
        'types.ChannelFull',
        alias='_'
    )

    id: int
    about: str
    read_inbox_max_id: int
    read_outbox_max_id: int
    unread_count: int
    chat_photo: "base.Photo"
    notify_settings: "base.PeerNotifySettings"
    bot_info: list["base.BotInfo"]
    pts: int
    can_view_participants: typing.Optional[bool] = None
    can_set_username: typing.Optional[bool] = None
    can_set_stickers: typing.Optional[bool] = None
    hidden_prehistory: typing.Optional[bool] = None
    can_set_location: typing.Optional[bool] = None
    has_scheduled: typing.Optional[bool] = None
    can_view_stats: typing.Optional[bool] = None
    blocked: typing.Optional[bool] = None
    can_delete_channel: typing.Optional[bool] = None
    antispam: typing.Optional[bool] = None
    participants_hidden: typing.Optional[bool] = None
    translations_disabled: typing.Optional[bool] = None
    stories_pinned_available: typing.Optional[bool] = None
    view_forum_as_messages: typing.Optional[bool] = None
    restricted_sponsored: typing.Optional[bool] = None
    can_view_revenue: typing.Optional[bool] = None
    participants_count: typing.Optional[int] = None
    admins_count: typing.Optional[int] = None
    kicked_count: typing.Optional[int] = None
    banned_count: typing.Optional[int] = None
    online_count: typing.Optional[int] = None
    exported_invite: typing.Optional["base.ExportedChatInvite"] = None
    migrated_from_chat_id: typing.Optional[int] = None
    migrated_from_max_id: typing.Optional[int] = None
    pinned_msg_id: typing.Optional[int] = None
    stickerset: typing.Optional["base.StickerSet"] = None
    available_min_id: typing.Optional[int] = None
    folder_id: typing.Optional[int] = None
    linked_chat_id: typing.Optional[int] = None
    location: typing.Optional["base.ChannelLocation"] = None
    slowmode_seconds: typing.Optional[int] = None
    slowmode_next_send_date: typing.Optional[Datetime] = None
    stats_dc: typing.Optional[int] = None
    call: typing.Optional["base.InputGroupCall"] = None
    ttl_period: typing.Optional[int] = None
    pending_suggestions: typing.Optional[list[str]] = None
    groupcall_default_join_as: typing.Optional["base.Peer"] = None
    theme_emoticon: typing.Optional[str] = None
    requests_pending: typing.Optional[int] = None
    recent_requesters: typing.Optional[list[int]] = None
    default_send_as: typing.Optional["base.Peer"] = None
    available_reactions: typing.Optional["base.ChatReactions"] = None
    reactions_limit: typing.Optional[int] = None
    stories: typing.Optional["base.PeerStories"] = None
    wallpaper: typing.Optional["base.WallPaper"] = None
    boosts_applied: typing.Optional[int] = None
    boosts_unrestrict: typing.Optional[int] = None
    emojiset: typing.Optional["base.StickerSet"] = None
