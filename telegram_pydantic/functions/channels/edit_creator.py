from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EditCreator(BaseModel):
    """
    functions.channels.EditCreator
    ID: 0x8f38cd1f
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.EditCreator', 'EditCreator'] = pydantic.Field(
        'functions.channels.EditCreator',
        alias='_'
    )

    channel: "base.InputChannel"
    user_id: "base.InputUser"
    password: "base.InputCheckPasswordSRP"
