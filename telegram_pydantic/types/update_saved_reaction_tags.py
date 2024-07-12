from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateSavedReactionTags(BaseModel):
    """
    types.UpdateSavedReactionTags
    ID: 0x39c67432
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateSavedReactionTags', 'UpdateSavedReactionTags'] = pydantic.Field(
        'types.UpdateSavedReactionTags',
        alias='_'
    )

