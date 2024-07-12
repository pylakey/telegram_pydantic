from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CodeTypeMissedCall(BaseModel):
    """
    types.auth.CodeTypeMissedCall
    ID: 0xd61ad6ee
    Layer: 181
    """
    QUALNAME: typing.Literal['types.auth.CodeTypeMissedCall', 'CodeTypeMissedCall'] = pydantic.Field(
        'types.auth.CodeTypeMissedCall',
        alias='_'
    )

