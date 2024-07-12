from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class IsEligibleToJoin(BaseModel):
    """
    functions.smsjobs.IsEligibleToJoin
    ID: 0xedc39d0
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.smsjobs.IsEligibleToJoin', 'IsEligibleToJoin'] = pydantic.Field(
        'functions.smsjobs.IsEligibleToJoin',
        alias='_'
    )

