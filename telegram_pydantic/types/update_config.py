from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateConfig(BaseModel):
    """
    types.UpdateConfig
    ID: 0xa229dd06
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateConfig', 'UpdateConfig'] = pydantic.Field(
        'types.UpdateConfig',
        alias='_'
    )

