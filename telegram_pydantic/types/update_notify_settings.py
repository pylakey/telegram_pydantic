from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateNotifySettings(BaseModel):
    """
    types.UpdateNotifySettings
    ID: 0xbec268ef
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateNotifySettings', 'UpdateNotifySettings'] = pydantic.Field(
        'types.UpdateNotifySettings',
        alias='_'
    )

    peer: "base.NotifyPeer"
    notify_settings: "base.PeerNotifySettings"
