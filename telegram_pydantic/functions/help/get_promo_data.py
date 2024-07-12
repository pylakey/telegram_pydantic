from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetPromoData(BaseModel):
    """
    functions.help.GetPromoData
    ID: 0xc0977421
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.help.GetPromoData', 'GetPromoData'] = pydantic.Field(
        'functions.help.GetPromoData',
        alias='_'
    )

