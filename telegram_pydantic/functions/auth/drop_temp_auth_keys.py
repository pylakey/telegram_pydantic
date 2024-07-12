from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DropTempAuthKeys(BaseModel):
    """
    functions.auth.DropTempAuthKeys
    ID: 0x8e48a188
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.auth.DropTempAuthKeys', 'DropTempAuthKeys'] = pydantic.Field(
        'functions.auth.DropTempAuthKeys',
        alias='_'
    )

    except_auth_keys: list[int]
