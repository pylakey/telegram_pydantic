from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class FileGif(BaseModel):
    """
    types.storage.FileGif
    ID: 0xcae1aadf
    Layer: 181
    """
    QUALNAME: typing.Literal['types.storage.FileGif', 'FileGif'] = pydantic.Field(
        'types.storage.FileGif',
        alias='_'
    )

