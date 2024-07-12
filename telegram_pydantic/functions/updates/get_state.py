from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetState(BaseModel):
    """
    functions.updates.GetState
    ID: 0xedd4882a
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.updates.GetState', 'GetState'] = pydantic.Field(
        'functions.updates.GetState',
        alias='_'
    )

