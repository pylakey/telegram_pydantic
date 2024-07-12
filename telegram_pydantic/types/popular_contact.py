from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PopularContact(BaseModel):
    """
    types.PopularContact
    ID: 0x5ce14175
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PopularContact', 'PopularContact'] = pydantic.Field(
        'types.PopularContact',
        alias='_'
    )

    client_id: int
    importers: int
