from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetPremiumPromo(BaseModel):
    """
    functions.help.GetPremiumPromo
    ID: 0xb81b93d4
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.help.GetPremiumPromo', 'GetPremiumPromo'] = pydantic.Field(
        'functions.help.GetPremiumPromo',
        alias='_'
    )

