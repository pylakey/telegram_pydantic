from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AllStickersNotModified(BaseModel):
    """
    types.messages.AllStickersNotModified
    ID: 0xe86602c3
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.AllStickersNotModified', 'AllStickersNotModified'] = pydantic.Field(
        'types.messages.AllStickersNotModified',
        alias='_'
    )

