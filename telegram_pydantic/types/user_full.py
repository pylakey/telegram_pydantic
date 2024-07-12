from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UserFull(BaseModel):
    """
    types.UserFull
    ID: 0xcc997720
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UserFull', 'UserFull'] = pydantic.Field(
        'types.UserFull',
        alias='_'
    )

    id: int
    settings: "base.PeerSettings"
    notify_settings: "base.PeerNotifySettings"
    common_chats_count: int
    blocked: typing.Optional[bool] = None
    phone_calls_available: typing.Optional[bool] = None
    phone_calls_private: typing.Optional[bool] = None
    can_pin_message: typing.Optional[bool] = None
    has_scheduled: typing.Optional[bool] = None
    video_calls_available: typing.Optional[bool] = None
    voice_messages_forbidden: typing.Optional[bool] = None
    translations_disabled: typing.Optional[bool] = None
    stories_pinned_available: typing.Optional[bool] = None
    blocked_my_stories_from: typing.Optional[bool] = None
    wallpaper_overridden: typing.Optional[bool] = None
    contact_require_premium: typing.Optional[bool] = None
    read_dates_private: typing.Optional[bool] = None
    sponsored_enabled: typing.Optional[bool] = None
    about: typing.Optional[str] = None
    personal_photo: typing.Optional["base.Photo"] = None
    profile_photo: typing.Optional["base.Photo"] = None
    fallback_photo: typing.Optional["base.Photo"] = None
    bot_info: typing.Optional["base.BotInfo"] = None
    pinned_msg_id: typing.Optional[int] = None
    folder_id: typing.Optional[int] = None
    ttl_period: typing.Optional[int] = None
    theme_emoticon: typing.Optional[str] = None
    private_forward_name: typing.Optional[str] = None
    bot_group_admin_rights: typing.Optional["base.ChatAdminRights"] = None
    bot_broadcast_admin_rights: typing.Optional["base.ChatAdminRights"] = None
    premium_gifts: typing.Optional[list["base.PremiumGiftOption"]] = None
    wallpaper: typing.Optional["base.WallPaper"] = None
    stories: typing.Optional["base.PeerStories"] = None
    business_work_hours: typing.Optional["base.BusinessWorkHours"] = None
    business_location: typing.Optional["base.BusinessLocation"] = None
    business_greeting_message: typing.Optional["base.BusinessGreetingMessage"] = None
    business_away_message: typing.Optional["base.BusinessAwayMessage"] = None
    business_intro: typing.Optional["base.BusinessIntro"] = None
    birthday: typing.Optional["base.Birthday"] = None
    personal_channel_id: typing.Optional[int] = None
    personal_channel_message: typing.Optional[int] = None
