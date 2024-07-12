from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateDialogFilterOrder(BaseModel):
    """
    types.UpdateDialogFilterOrder
    ID: 0xa5d72105
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateDialogFilterOrder', 'UpdateDialogFilterOrder'] = pydantic.Field(
        'types.UpdateDialogFilterOrder',
        alias='_'
    )

    order: list[int]
