from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PaymentForm(BaseModel):
    """
    types.payments.PaymentForm
    ID: 0xa0058751
    Layer: 181
    """
    QUALNAME: typing.Literal['types.payments.PaymentForm', 'PaymentForm'] = pydantic.Field(
        'types.payments.PaymentForm',
        alias='_'
    )

    form_id: int
    bot_id: int
    title: str
    description: str
    invoice: "base.Invoice"
    provider_id: int
    url: str
    users: list["base.User"]
    can_save_credentials: typing.Optional[bool] = None
    password_missing: typing.Optional[bool] = None
    photo: typing.Optional["base.WebDocument"] = None
    native_provider: typing.Optional[str] = None
    native_params: typing.Optional["base.DataJSON"] = None
    additional_methods: typing.Optional[list["base.PaymentFormMethod"]] = None
    saved_info: typing.Optional["base.PaymentRequestedInfo"] = None
    saved_credentials: typing.Optional[list["base.PaymentSavedCredentials"]] = None
