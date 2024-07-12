from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetDocumentByHash(BaseModel):
    """
    functions.messages.GetDocumentByHash
    ID: 0xb1f2061f
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetDocumentByHash', 'GetDocumentByHash'] = pydantic.Field(
        'functions.messages.GetDocumentByHash',
        alias='_'
    )

    sha256: Bytes
    size: int
    mime_type: str
