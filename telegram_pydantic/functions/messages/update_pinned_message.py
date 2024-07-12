from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdatePinnedMessage(BaseModel):
    """
    functions.messages.UpdatePinnedMessage
    ID: 0xd2aaf7ec
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.UpdatePinnedMessage', 'UpdatePinnedMessage'] = pydantic.Field(
        'functions.messages.UpdatePinnedMessage',
        alias='_'
    )

    peer: "base.InputPeer"
    id: int
    silent: typing.Optional[bool] = None
    unpin: typing.Optional[bool] = None
    pm_oneside: typing.Optional[bool] = None
