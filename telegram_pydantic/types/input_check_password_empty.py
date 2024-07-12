from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputCheckPasswordEmpty(BaseModel):
    """
    types.InputCheckPasswordEmpty
    ID: 0x9880f658
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputCheckPasswordEmpty', 'InputCheckPasswordEmpty'] = pydantic.Field(
        'types.InputCheckPasswordEmpty',
        alias='_'
    )

