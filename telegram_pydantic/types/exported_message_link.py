from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ExportedMessageLink(BaseModel):
    """
    types.ExportedMessageLink
    ID: 0x5dab1af4
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ExportedMessageLink', 'ExportedMessageLink'] = pydantic.Field(
        'types.ExportedMessageLink',
        alias='_'
    )

    link: str
    html: str
