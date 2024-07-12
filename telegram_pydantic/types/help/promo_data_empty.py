from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PromoDataEmpty(BaseModel):
    """
    types.help.PromoDataEmpty
    ID: 0x98f6ac75
    Layer: 181
    """
    QUALNAME: typing.Literal['types.help.PromoDataEmpty', 'PromoDataEmpty'] = pydantic.Field(
        'types.help.PromoDataEmpty',
        alias='_'
    )

    expires: Datetime
