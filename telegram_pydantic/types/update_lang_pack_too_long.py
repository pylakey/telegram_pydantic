from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateLangPackTooLong(BaseModel):
    """
    types.UpdateLangPackTooLong
    ID: 0x46560264
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateLangPackTooLong', 'UpdateLangPackTooLong'] = pydantic.Field(
        'types.UpdateLangPackTooLong',
        alias='_'
    )

    lang_code: str
