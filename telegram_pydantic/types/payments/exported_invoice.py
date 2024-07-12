from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ExportedInvoice(BaseModel):
    """
    types.payments.ExportedInvoice
    ID: 0xaed0cbd9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.payments.ExportedInvoice', 'ExportedInvoice'] = pydantic.Field(
        'types.payments.ExportedInvoice',
        alias='_'
    )

    url: str
