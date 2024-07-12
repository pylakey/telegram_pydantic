from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EmailVerifyPurposeLoginChange(BaseModel):
    """
    types.EmailVerifyPurposeLoginChange
    ID: 0x527d22eb
    Layer: 181
    """
    QUALNAME: typing.Literal['types.EmailVerifyPurposeLoginChange', 'EmailVerifyPurposeLoginChange'] = pydantic.Field(
        'types.EmailVerifyPurposeLoginChange',
        alias='_'
    )

