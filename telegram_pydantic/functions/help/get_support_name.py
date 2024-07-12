from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetSupportName(BaseModel):
    """
    functions.help.GetSupportName
    ID: 0xd360e72c
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.help.GetSupportName', 'GetSupportName'] = pydantic.Field(
        'functions.help.GetSupportName',
        alias='_'
    )

