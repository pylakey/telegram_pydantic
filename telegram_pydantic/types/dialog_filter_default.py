from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DialogFilterDefault(BaseModel):
    """
    types.DialogFilterDefault
    ID: 0x363293ae
    Layer: 181
    """
    QUALNAME: typing.Literal['types.DialogFilterDefault', 'DialogFilterDefault'] = pydantic.Field(
        'types.DialogFilterDefault',
        alias='_'
    )

