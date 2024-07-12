from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BotResults(BaseModel):
    """
    types.messages.BotResults
    ID: 0xe021f2f6
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.BotResults', 'BotResults'] = pydantic.Field(
        'types.messages.BotResults',
        alias='_'
    )

    query_id: int
    results: list["base.BotInlineResult"]
    cache_time: int
    users: list["base.User"]
    gallery: typing.Optional[bool] = None
    next_offset: typing.Optional[str] = None
    switch_pm: typing.Optional["base.InlineBotSwitchPM"] = None
    switch_webview: typing.Optional["base.InlineBotWebView"] = None
