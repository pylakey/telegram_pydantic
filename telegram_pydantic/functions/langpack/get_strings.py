from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetStrings(BaseModel):
    """
    functions.langpack.GetStrings
    ID: 0xefea3803
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.langpack.GetStrings', 'GetStrings'] = pydantic.Field(
        'functions.langpack.GetStrings',
        alias='_'
    )

    lang_pack: str
    lang_code: str
    keys: list[str]
