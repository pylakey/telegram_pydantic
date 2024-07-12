from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecureRequiredType(BaseModel):
    """
    types.SecureRequiredType
    ID: 0x829d99da
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecureRequiredType', 'SecureRequiredType'] = pydantic.Field(
        'types.SecureRequiredType',
        alias='_'
    )

    type: "base.SecureValueType"
    native_names: typing.Optional[bool] = None
    selfie_required: typing.Optional[bool] = None
    translation_required: typing.Optional[bool] = None
