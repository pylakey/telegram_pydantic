from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateSavedGifs(BaseModel):
    """
    types.UpdateSavedGifs
    ID: 0x9375341e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateSavedGifs', 'UpdateSavedGifs'] = pydantic.Field(
        'types.UpdateSavedGifs',
        alias='_'
    )

