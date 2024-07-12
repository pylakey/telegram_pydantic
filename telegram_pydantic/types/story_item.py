from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StoryItem(BaseModel):
    """
    types.StoryItem
    ID: 0x79b26a24
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StoryItem', 'StoryItem'] = pydantic.Field(
        'types.StoryItem',
        alias='_'
    )

    id: int
    date: Datetime
    expire_date: Datetime
    media: "base.MessageMedia"
    pinned: typing.Optional[bool] = None
    public: typing.Optional[bool] = None
    close_friends: typing.Optional[bool] = None
    min: typing.Optional[bool] = None
    noforwards: typing.Optional[bool] = None
    edited: typing.Optional[bool] = None
    contacts: typing.Optional[bool] = None
    selected_contacts: typing.Optional[bool] = None
    out: typing.Optional[bool] = None
    from_id: typing.Optional["base.Peer"] = None
    fwd_from: typing.Optional["base.StoryFwdHeader"] = None
    caption: typing.Optional[str] = None
    entities: typing.Optional[list["base.MessageEntity"]] = None
    media_areas: typing.Optional[list["base.MediaArea"]] = None
    privacy: typing.Optional[list["base.PrivacyRule"]] = None
    views: typing.Optional["base.StoryViews"] = None
    sent_reaction: typing.Optional["base.Reaction"] = None
