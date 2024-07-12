from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CodeTypeFlashCall(BaseModel):
    """
    types.auth.CodeTypeFlashCall
    ID: 0x226ccefb
    Layer: 181
    """
    QUALNAME: typing.Literal['types.auth.CodeTypeFlashCall', 'CodeTypeFlashCall'] = pydantic.Field(
        'types.auth.CodeTypeFlashCall',
        alias='_'
    )

