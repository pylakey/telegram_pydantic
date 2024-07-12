from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendStory(BaseModel):
    """
    functions.stories.SendStory
    ID: 0xe4e6694b
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stories.SendStory', 'SendStory'] = pydantic.Field(
        'functions.stories.SendStory',
        alias='_'
    )

    peer: "base.InputPeer"
    media: "base.InputMedia"
    privacy_rules: list["base.InputPrivacyRule"]
    random_id: int
    pinned: typing.Optional[bool] = None
    noforwards: typing.Optional[bool] = None
    fwd_modified: typing.Optional[bool] = None
    media_areas: typing.Optional[list["base.MediaArea"]] = None
    caption: typing.Optional[str] = None
    entities: typing.Optional[list["base.MessageEntity"]] = None
    period: typing.Optional[int] = None
    fwd_from_id: typing.Optional["base.InputPeer"] = None
    fwd_from_story: typing.Optional[int] = None
