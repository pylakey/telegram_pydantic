from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChatFull(BaseModel):
    """
    types.ChatFull
    ID: 0x2633421b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChatFull', 'ChatFull'] = pydantic.Field(
        'types.ChatFull',
        alias='_'
    )

    id: int
    about: str
    participants: "base.ChatParticipants"
    notify_settings: "base.PeerNotifySettings"
    can_set_username: typing.Optional[bool] = None
    has_scheduled: typing.Optional[bool] = None
    translations_disabled: typing.Optional[bool] = None
    chat_photo: typing.Optional["base.Photo"] = None
    exported_invite: typing.Optional["base.ExportedChatInvite"] = None
    bot_info: typing.Optional[list["base.BotInfo"]] = None
    pinned_msg_id: typing.Optional[int] = None
    folder_id: typing.Optional[int] = None
    call: typing.Optional["base.InputGroupCall"] = None
    ttl_period: typing.Optional[int] = None
    groupcall_default_join_as: typing.Optional["base.Peer"] = None
    theme_emoticon: typing.Optional[str] = None
    requests_pending: typing.Optional[int] = None
    recent_requesters: typing.Optional[list[int]] = None
    available_reactions: typing.Optional["base.ChatReactions"] = None
    reactions_limit: typing.Optional[int] = None
