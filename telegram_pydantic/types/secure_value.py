from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecureValue(BaseModel):
    """
    types.SecureValue
    ID: 0x187fa0ca
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecureValue', 'SecureValue'] = pydantic.Field(
        'types.SecureValue',
        alias='_'
    )

    type: "base.SecureValueType"
    hash: Bytes
    data: typing.Optional["base.SecureData"] = None
    front_side: typing.Optional["base.SecureFile"] = None
    reverse_side: typing.Optional["base.SecureFile"] = None
    selfie: typing.Optional["base.SecureFile"] = None
    translation: typing.Optional[list["base.SecureFile"]] = None
    files: typing.Optional[list["base.SecureFile"]] = None
    plain_data: typing.Optional["base.SecurePlainData"] = None
