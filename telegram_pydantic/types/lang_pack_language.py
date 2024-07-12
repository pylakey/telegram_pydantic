from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class LangPackLanguage(BaseModel):
    """
    types.LangPackLanguage
    ID: 0xeeca5ce3
    Layer: 181
    """
    QUALNAME: typing.Literal['types.LangPackLanguage', 'LangPackLanguage'] = pydantic.Field(
        'types.LangPackLanguage',
        alias='_'
    )

    name: str
    native_name: str
    lang_code: str
    plural_code: str
    strings_count: int
    translated_count: int
    translations_url: str
    official: typing.Optional[bool] = None
    rtl: typing.Optional[bool] = None
    beta: typing.Optional[bool] = None
    base_lang_code: typing.Optional[str] = None
