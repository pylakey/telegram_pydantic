from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class FilePartial(BaseModel):
    """
    types.storage.FilePartial
    ID: 0x40bc6f52
    Layer: 181
    """
    QUALNAME: typing.Literal['types.storage.FilePartial', 'FilePartial'] = pydantic.Field(
        'types.storage.FilePartial',
        alias='_'
    )

