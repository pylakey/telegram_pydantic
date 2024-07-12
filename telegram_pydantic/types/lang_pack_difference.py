from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class LangPackDifference(BaseModel):
    """
    types.LangPackDifference
    ID: 0xf385c1f6
    Layer: 181
    """
    QUALNAME: typing.Literal['types.LangPackDifference', 'LangPackDifference'] = pydantic.Field(
        'types.LangPackDifference',
        alias='_'
    )

    lang_code: str
    from_version: int
    version: int
    strings: list["base.LangPackString"]
