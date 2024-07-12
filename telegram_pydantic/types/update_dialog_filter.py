from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateDialogFilter(BaseModel):
    """
    types.UpdateDialogFilter
    ID: 0x26ffde7d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateDialogFilter', 'UpdateDialogFilter'] = pydantic.Field(
        'types.UpdateDialogFilter',
        alias='_'
    )

    id: int
    filter: typing.Optional["base.DialogFilter"] = None
