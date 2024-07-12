from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputDocumentEmpty(BaseModel):
    """
    types.InputDocumentEmpty
    ID: 0x72f0eaae
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputDocumentEmpty', 'InputDocumentEmpty'] = pydantic.Field(
        'types.InputDocumentEmpty',
        alias='_'
    )

