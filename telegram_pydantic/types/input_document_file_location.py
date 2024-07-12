from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputDocumentFileLocation(BaseModel):
    """
    types.InputDocumentFileLocation
    ID: 0xbad07584
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputDocumentFileLocation', 'InputDocumentFileLocation'] = pydantic.Field(
        'types.InputDocumentFileLocation',
        alias='_'
    )

    id: int
    access_hash: int
    file_reference: Bytes
    thumb_size: str
