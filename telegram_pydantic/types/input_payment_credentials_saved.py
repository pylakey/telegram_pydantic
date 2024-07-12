from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPaymentCredentialsSaved(BaseModel):
    """
    types.InputPaymentCredentialsSaved
    ID: 0xc10eb2cf
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPaymentCredentialsSaved', 'InputPaymentCredentialsSaved'] = pydantic.Field(
        'types.InputPaymentCredentialsSaved',
        alias='_'
    )

    id: str
    tmp_password: Bytes
