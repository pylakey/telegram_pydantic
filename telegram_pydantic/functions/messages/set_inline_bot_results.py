from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SetInlineBotResults(BaseModel):
    """
    functions.messages.SetInlineBotResults
    ID: 0xbb12a419
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.SetInlineBotResults', 'SetInlineBotResults'] = pydantic.Field(
        'functions.messages.SetInlineBotResults',
        alias='_'
    )

    query_id: int
    results: list["base.InputBotInlineResult"]
    cache_time: int
    gallery: typing.Optional[bool] = None
    private: typing.Optional[bool] = None
    next_offset: typing.Optional[str] = None
    switch_pm: typing.Optional["base.InlineBotSwitchPM"] = None
    switch_webview: typing.Optional["base.InlineBotWebView"] = None
