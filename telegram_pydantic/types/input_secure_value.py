from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputSecureValue(BaseModel):
    """
    types.InputSecureValue
    ID: 0xdb21d0a7
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputSecureValue', 'InputSecureValue'] = pydantic.Field(
        'types.InputSecureValue',
        alias='_'
    )

    type: "base.SecureValueType"
    data: typing.Optional["base.SecureData"] = None
    front_side: typing.Optional["base.InputSecureFile"] = None
    reverse_side: typing.Optional["base.InputSecureFile"] = None
    selfie: typing.Optional["base.InputSecureFile"] = None
    translation: typing.Optional[list["base.InputSecureFile"]] = None
    files: typing.Optional[list["base.InputSecureFile"]] = None
    plain_data: typing.Optional["base.SecurePlainData"] = None
