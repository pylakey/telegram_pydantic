from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class User(BaseModel):
    """
    types.User
    ID: 0x215c4438
    Layer: 181
    """
    QUALNAME: typing.Literal['types.User', 'User'] = pydantic.Field(
        'types.User',
        alias='_'
    )

    id: int
    is_self: typing.Optional[bool] = pydantic.Field(
        None,
        serialization_alias='self',
        validation_alias=pydantic.AliasChoices('self', 'is_self')
    )
    contact: typing.Optional[bool] = None
    mutual_contact: typing.Optional[bool] = None
    deleted: typing.Optional[bool] = None
    bot: typing.Optional[bool] = None
    bot_chat_history: typing.Optional[bool] = None
    bot_nochats: typing.Optional[bool] = None
    verified: typing.Optional[bool] = None
    restricted: typing.Optional[bool] = None
    min: typing.Optional[bool] = None
    bot_inline_geo: typing.Optional[bool] = None
    support: typing.Optional[bool] = None
    scam: typing.Optional[bool] = None
    apply_min_photo: typing.Optional[bool] = None
    fake: typing.Optional[bool] = None
    bot_attach_menu: typing.Optional[bool] = None
    premium: typing.Optional[bool] = None
    attach_menu_enabled: typing.Optional[bool] = None
    bot_can_edit: typing.Optional[bool] = None
    close_friend: typing.Optional[bool] = None
    stories_hidden: typing.Optional[bool] = None
    stories_unavailable: typing.Optional[bool] = None
    contact_require_premium: typing.Optional[bool] = None
    bot_business: typing.Optional[bool] = None
    access_hash: typing.Optional[int] = None
    first_name: typing.Optional[str] = None
    last_name: typing.Optional[str] = None
    username: typing.Optional[str] = None
    phone: typing.Optional[str] = None
    photo: typing.Optional["base.UserProfilePhoto"] = None
    status: typing.Optional["base.UserStatus"] = None
    bot_info_version: typing.Optional[int] = None
    restriction_reason: typing.Optional[list["base.RestrictionReason"]] = None
    bot_inline_placeholder: typing.Optional[str] = None
    lang_code: typing.Optional[str] = None
    emoji_status: typing.Optional["base.EmojiStatus"] = None
    usernames: typing.Optional[list["base.Username"]] = None
    stories_max_id: typing.Optional[int] = None
    color: typing.Optional["base.PeerColor"] = None
    profile_color: typing.Optional["base.PeerColor"] = None
