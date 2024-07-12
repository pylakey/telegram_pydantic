from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SaveAutoSaveSettings(BaseModel):
    """
    functions.account.SaveAutoSaveSettings
    ID: 0xd69b8361
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.SaveAutoSaveSettings', 'SaveAutoSaveSettings'] = pydantic.Field(
        'functions.account.SaveAutoSaveSettings',
        alias='_'
    )

    settings: "base.AutoSaveSettings"
    users: typing.Optional[bool] = None
    chats: typing.Optional[bool] = None
    broadcasts: typing.Optional[bool] = None
    peer: typing.Optional["base.InputPeer"] = None
