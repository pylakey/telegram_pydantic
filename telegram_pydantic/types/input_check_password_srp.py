from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputCheckPasswordSRP(BaseModel):
    """
    types.InputCheckPasswordSRP
    ID: 0xd27ff082
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputCheckPasswordSRP', 'InputCheckPasswordSRP'] = pydantic.Field(
        'types.InputCheckPasswordSRP',
        alias='_'
    )

    srp_id: int
    A: Bytes
    M1: Bytes
