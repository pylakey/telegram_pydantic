from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SupportName(BaseModel):
    """
    types.help.SupportName
    ID: 0x8c05f1c9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.help.SupportName', 'SupportName'] = pydantic.Field(
        'types.help.SupportName',
        alias='_'
    )

    name: str
