from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetLangPack(BaseModel):
    """
    functions.langpack.GetLangPack
    ID: 0xf2f2330a
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.langpack.GetLangPack', 'GetLangPack'] = pydantic.Field(
        'functions.langpack.GetLangPack',
        alias='_'
    )

    lang_pack: str
    lang_code: str
