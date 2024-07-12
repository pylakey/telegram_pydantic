from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EditPhoto(BaseModel):
    """
    functions.channels.EditPhoto
    ID: 0xf12e57c9
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.EditPhoto', 'EditPhoto'] = pydantic.Field(
        'functions.channels.EditPhoto',
        alias='_'
    )

    channel: "base.InputChannel"
    photo: "base.InputChatPhoto"
