from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputFileLocation(BaseModel):
    """
    types.InputFileLocation
    ID: 0xdfdaabe1
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputFileLocation', 'InputFileLocation'] = pydantic.Field(
        'types.InputFileLocation',
        alias='_'
    )

    volume_id: int
    local_id: int
    secret: int
    file_reference: Bytes
