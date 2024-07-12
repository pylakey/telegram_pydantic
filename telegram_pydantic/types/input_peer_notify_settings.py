from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPeerNotifySettings(BaseModel):
    """
    types.InputPeerNotifySettings
    ID: 0xcacb6ae2
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPeerNotifySettings', 'InputPeerNotifySettings'] = pydantic.Field(
        'types.InputPeerNotifySettings',
        alias='_'
    )

    show_previews: typing.Optional[bool] = None
    silent: typing.Optional[bool] = None
    mute_until: typing.Optional[Datetime] = None
    sound: typing.Optional["base.NotificationSound"] = None
    stories_muted: typing.Optional[bool] = None
    stories_hide_sender: typing.Optional[bool] = None
    stories_sound: typing.Optional["base.NotificationSound"] = None
