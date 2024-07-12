from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateDialogFilters(BaseModel):
    """
    types.UpdateDialogFilters
    ID: 0x3504914f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateDialogFilters', 'UpdateDialogFilters'] = pydantic.Field(
        'types.UpdateDialogFilters',
        alias='_'
    )

