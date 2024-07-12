from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendStarsForm(BaseModel):
    """
    functions.payments.SendStarsForm
    ID: 0x2bb731d
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.payments.SendStarsForm', 'SendStarsForm'] = pydantic.Field(
        'functions.payments.SendStarsForm',
        alias='_'
    )

    form_id: int
    invoice: "base.InputInvoice"
