from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ForumTopicDeleted(BaseModel):
    """
    types.ForumTopicDeleted
    ID: 0x23f109b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ForumTopicDeleted', 'ForumTopicDeleted'] = pydantic.Field(
        'types.ForumTopicDeleted',
        alias='_'
    )

    id: int
