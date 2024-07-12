from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Join(BaseModel):
    """
    functions.smsjobs.Join
    ID: 0xa74ece2d
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.smsjobs.Join', 'Join'] = pydantic.Field(
        'functions.smsjobs.Join',
        alias='_'
    )

