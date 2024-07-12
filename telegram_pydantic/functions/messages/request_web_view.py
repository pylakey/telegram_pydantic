from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class RequestWebView(BaseModel):
    """
    functions.messages.RequestWebView
    ID: 0x269dc2c1
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.RequestWebView', 'RequestWebView'] = pydantic.Field(
        'functions.messages.RequestWebView',
        alias='_'
    )

    peer: "base.InputPeer"
    bot: "base.InputUser"
    platform: str
    from_bot_menu: typing.Optional[bool] = None
    silent: typing.Optional[bool] = None
    url: typing.Optional[str] = None
    start_param: typing.Optional[str] = None
    theme_params: typing.Optional["base.DataJSON"] = None
    reply_to: typing.Optional["base.InputReplyTo"] = None
    send_as: typing.Optional["base.InputPeer"] = None
