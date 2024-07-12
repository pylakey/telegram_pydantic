from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class NoAppUpdate(BaseModel):
    """
    types.help.NoAppUpdate
    ID: 0xc45a6536
    Layer: 181
    """
    QUALNAME: typing.Literal['types.help.NoAppUpdate', 'NoAppUpdate'] = pydantic.Field(
        'types.help.NoAppUpdate',
        alias='_'
    )

