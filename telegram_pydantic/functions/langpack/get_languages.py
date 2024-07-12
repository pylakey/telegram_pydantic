from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetLanguages(BaseModel):
    """
    functions.langpack.GetLanguages
    ID: 0x42c6978f
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.langpack.GetLanguages', 'GetLanguages'] = pydantic.Field(
        'functions.langpack.GetLanguages',
        alias='_'
    )

    lang_pack: str
