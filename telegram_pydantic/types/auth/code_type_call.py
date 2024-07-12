from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CodeTypeCall(BaseModel):
    """
    types.auth.CodeTypeCall
    ID: 0x741cd3e3
    Layer: 181
    """
    QUALNAME: typing.Literal['types.auth.CodeTypeCall', 'CodeTypeCall'] = pydantic.Field(
        'types.auth.CodeTypeCall',
        alias='_'
    )

