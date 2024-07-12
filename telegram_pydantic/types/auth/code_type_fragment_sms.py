from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CodeTypeFragmentSms(BaseModel):
    """
    types.auth.CodeTypeFragmentSms
    ID: 0x6ed998c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.auth.CodeTypeFragmentSms', 'CodeTypeFragmentSms'] = pydantic.Field(
        'types.auth.CodeTypeFragmentSms',
        alias='_'
    )

