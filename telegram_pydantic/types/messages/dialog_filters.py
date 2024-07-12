from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DialogFilters(BaseModel):
    """
    types.messages.DialogFilters
    ID: 0x2ad93719
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.DialogFilters', 'DialogFilters'] = pydantic.Field(
        'types.messages.DialogFilters',
        alias='_'
    )

    filters: list["base.DialogFilter"]
    tags_enabled: typing.Optional[bool] = None
