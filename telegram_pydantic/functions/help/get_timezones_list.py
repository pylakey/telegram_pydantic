from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetTimezonesList(BaseModel):
    """
    functions.help.GetTimezonesList
    ID: 0x49b30240
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.help.GetTimezonesList', 'GetTimezonesList'] = pydantic.Field(
        'functions.help.GetTimezonesList',
        alias='_'
    )

    hash: int
