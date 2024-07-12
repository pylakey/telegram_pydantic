from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChatAdminRights(BaseModel):
    """
    types.ChatAdminRights
    ID: 0x5fb224d5
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChatAdminRights', 'ChatAdminRights'] = pydantic.Field(
        'types.ChatAdminRights',
        alias='_'
    )

    change_info: typing.Optional[bool] = None
    post_messages: typing.Optional[bool] = None
    edit_messages: typing.Optional[bool] = None
    delete_messages: typing.Optional[bool] = None
    ban_users: typing.Optional[bool] = None
    invite_users: typing.Optional[bool] = None
    pin_messages: typing.Optional[bool] = None
    add_admins: typing.Optional[bool] = None
    anonymous: typing.Optional[bool] = None
    manage_call: typing.Optional[bool] = None
    other: typing.Optional[bool] = None
    manage_topics: typing.Optional[bool] = None
    post_stories: typing.Optional[bool] = None
    edit_stories: typing.Optional[bool] = None
    delete_stories: typing.Optional[bool] = None
