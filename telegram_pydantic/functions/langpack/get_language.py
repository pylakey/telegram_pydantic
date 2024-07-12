from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetLanguage(BaseModel):
    """
    functions.langpack.GetLanguage
    ID: 0x6a596502
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.langpack.GetLanguage', 'GetLanguage'] = pydantic.Field(
        'functions.langpack.GetLanguage',
        alias='_'
    )

    lang_pack: str
    lang_code: str
