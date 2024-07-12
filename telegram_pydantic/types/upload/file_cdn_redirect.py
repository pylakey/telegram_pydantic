from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class FileCdnRedirect(BaseModel):
    """
    types.upload.FileCdnRedirect
    ID: 0xf18cda44
    Layer: 181
    """
    QUALNAME: typing.Literal['types.upload.FileCdnRedirect', 'FileCdnRedirect'] = pydantic.Field(
        'types.upload.FileCdnRedirect',
        alias='_'
    )

    dc_id: int
    file_token: Bytes
    encryption_key: Bytes
    encryption_iv: Bytes
    file_hashes: list["base.FileHash"]
