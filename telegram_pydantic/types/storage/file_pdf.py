from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class FilePdf(BaseModel):
    """
    types.storage.FilePdf
    ID: 0xae1e508d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.storage.FilePdf', 'FilePdf'] = pydantic.Field(
        'types.storage.FilePdf',
        alias='_'
    )

