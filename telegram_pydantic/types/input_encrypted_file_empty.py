from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputEncryptedFileEmpty(BaseModel):
    """
    types.InputEncryptedFileEmpty
    ID: 0x1837c364
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputEncryptedFileEmpty', 'InputEncryptedFileEmpty'] = pydantic.Field(
        'types.InputEncryptedFileEmpty',
        alias='_'
    )

