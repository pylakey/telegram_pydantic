from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateDialogFiltersOrder(BaseModel):
    """
    functions.messages.UpdateDialogFiltersOrder
    ID: 0xc563c1e4
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.UpdateDialogFiltersOrder', 'UpdateDialogFiltersOrder'] = pydantic.Field(
        'functions.messages.UpdateDialogFiltersOrder',
        alias='_'
    )

    order: list[int]
