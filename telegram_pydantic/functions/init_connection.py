from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InitConnection(BaseModel):
    """
    functions.InitConnection
    ID: 0xc1cd5ea9
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.InitConnection', 'InitConnection'] = pydantic.Field(
        'functions.InitConnection',
        alias='_'
    )

    api_id: int
    device_model: str
    system_version: str
    app_version: str
    system_lang_code: str
    lang_pack: str
    lang_code: str
    query: BaseModel
    proxy: typing.Optional["base.InputClientProxy"] = None
    params: typing.Optional["base.JSONValue"] = None
