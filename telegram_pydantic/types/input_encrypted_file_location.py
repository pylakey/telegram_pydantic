from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputEncryptedFileLocation(BaseModel):
    """
    types.InputEncryptedFileLocation
    ID: 0xf5235d55
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputEncryptedFileLocation', 'InputEncryptedFileLocation'] = pydantic.Field(
        'types.InputEncryptedFileLocation',
        alias='_'
    )

    id: int
    access_hash: int
