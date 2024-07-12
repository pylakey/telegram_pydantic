from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CdnFile(BaseModel):
    """
    types.upload.CdnFile
    ID: 0xa99fca4f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.upload.CdnFile', 'CdnFile'] = pydantic.Field(
        'types.upload.CdnFile',
        alias='_'
    )

    bytes: Bytes
