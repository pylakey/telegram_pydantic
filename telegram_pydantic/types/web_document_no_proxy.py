from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class WebDocumentNoProxy(BaseModel):
    """
    types.WebDocumentNoProxy
    ID: 0xf9c8bcc6
    Layer: 181
    """
    QUALNAME: typing.Literal['types.WebDocumentNoProxy', 'WebDocumentNoProxy'] = pydantic.Field(
        'types.WebDocumentNoProxy',
        alias='_'
    )

    url: str
    size: int
    mime_type: str
    attributes: list["base.DocumentAttribute"]
