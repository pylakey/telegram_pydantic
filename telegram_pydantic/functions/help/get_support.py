from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetSupport(BaseModel):
    """
    functions.help.GetSupport
    ID: 0x9cdf08cd
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.help.GetSupport', 'GetSupport'] = pydantic.Field(
        'functions.help.GetSupport',
        alias='_'
    )

