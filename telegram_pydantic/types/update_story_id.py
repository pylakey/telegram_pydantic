from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateStoryID(BaseModel):
    """
    types.UpdateStoryID
    ID: 0x1bf335b9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateStoryID', 'UpdateStoryID'] = pydantic.Field(
        'types.UpdateStoryID',
        alias='_'
    )

    id: int
    random_id: int
