from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetDifference(BaseModel):
    """
    functions.langpack.GetDifference
    ID: 0xcd984aa5
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.langpack.GetDifference', 'GetDifference'] = pydantic.Field(
        'functions.langpack.GetDifference',
        alias='_'
    )

    lang_pack: str
    lang_code: str
    from_version: int
