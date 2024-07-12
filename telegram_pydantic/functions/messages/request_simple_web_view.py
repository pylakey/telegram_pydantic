from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class RequestSimpleWebView(BaseModel):
    """
    functions.messages.RequestSimpleWebView
    ID: 0x1a46500a
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.RequestSimpleWebView', 'RequestSimpleWebView'] = pydantic.Field(
        'functions.messages.RequestSimpleWebView',
        alias='_'
    )

    bot: "base.InputUser"
    platform: str
    from_switch_webview: typing.Optional[bool] = None
    from_side_menu: typing.Optional[bool] = None
    url: typing.Optional[str] = None
    start_param: typing.Optional[str] = None
    theme_params: typing.Optional["base.DataJSON"] = None
