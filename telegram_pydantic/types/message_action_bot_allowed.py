from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionBotAllowed(BaseModel):
    """
    types.MessageActionBotAllowed
    ID: 0xc516d679
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionBotAllowed', 'MessageActionBotAllowed'] = pydantic.Field(
        'types.MessageActionBotAllowed',
        alias='_'
    )

    attach_menu: typing.Optional[bool] = None
    from_request: typing.Optional[bool] = None
    domain: typing.Optional[str] = None
    app: typing.Optional["base.BotApp"] = None
