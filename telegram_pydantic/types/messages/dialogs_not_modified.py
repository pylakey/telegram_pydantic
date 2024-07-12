from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DialogsNotModified(BaseModel):
    """
    types.messages.DialogsNotModified
    ID: 0xf0e3e596
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.DialogsNotModified', 'DialogsNotModified'] = pydantic.Field(
        'types.messages.DialogsNotModified',
        alias='_'
    )

    count: int
