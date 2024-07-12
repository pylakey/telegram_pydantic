from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ExportInvoice(BaseModel):
    """
    functions.payments.ExportInvoice
    ID: 0xf91b065
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.payments.ExportInvoice', 'ExportInvoice'] = pydantic.Field(
        'functions.payments.ExportInvoice',
        alias='_'
    )

    invoice_media: "base.InputMedia"
