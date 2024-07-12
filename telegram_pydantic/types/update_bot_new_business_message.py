from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateBotNewBusinessMessage(BaseModel):
    """
    types.UpdateBotNewBusinessMessage
    ID: 0x9ddb347c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateBotNewBusinessMessage', 'UpdateBotNewBusinessMessage'] = pydantic.Field(
        'types.UpdateBotNewBusinessMessage',
        alias='_'
    )

    connection_id: str
    message: "base.Message"
    qts: int
    reply_to_message: typing.Optional["base.Message"] = None
