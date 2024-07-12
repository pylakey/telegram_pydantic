from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class LangPackStringPluralized(BaseModel):
    """
    types.LangPackStringPluralized
    ID: 0x6c47ac9f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.LangPackStringPluralized', 'LangPackStringPluralized'] = pydantic.Field(
        'types.LangPackStringPluralized',
        alias='_'
    )

    key: str
    other_value: str
    zero_value: typing.Optional[str] = None
    one_value: typing.Optional[str] = None
    two_value: typing.Optional[str] = None
    few_value: typing.Optional[str] = None
    many_value: typing.Optional[str] = None
