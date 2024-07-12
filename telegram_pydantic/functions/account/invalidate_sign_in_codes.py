from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InvalidateSignInCodes(BaseModel):
    """
    functions.account.InvalidateSignInCodes
    ID: 0xca8ae8ba
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.InvalidateSignInCodes', 'InvalidateSignInCodes'] = pydantic.Field(
        'functions.account.InvalidateSignInCodes',
        alias='_'
    )

    codes: list[str]
