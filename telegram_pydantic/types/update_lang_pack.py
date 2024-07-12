from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateLangPack(BaseModel):
    """
    types.UpdateLangPack
    ID: 0x56022f4d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateLangPack', 'UpdateLangPack'] = pydantic.Field(
        'types.UpdateLangPack',
        alias='_'
    )

    difference: "base.LangPackDifference"
