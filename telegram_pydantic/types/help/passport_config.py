from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PassportConfig(BaseModel):
    """
    types.help.PassportConfig
    ID: 0xa098d6af
    Layer: 181
    """
    QUALNAME: typing.Literal['types.help.PassportConfig', 'PassportConfig'] = pydantic.Field(
        'types.help.PassportConfig',
        alias='_'
    )

    hash: int
    countries_langs: "base.DataJSON"
