from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMediaUploadedDocument(BaseModel):
    """
    types.InputMediaUploadedDocument
    ID: 0x5b38c6c1
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMediaUploadedDocument', 'InputMediaUploadedDocument'] = pydantic.Field(
        'types.InputMediaUploadedDocument',
        alias='_'
    )

    file: "base.InputFile"
    mime_type: str
    attributes: list["base.DocumentAttribute"]
    nosound_video: typing.Optional[bool] = None
    force_file: typing.Optional[bool] = None
    spoiler: typing.Optional[bool] = None
    thumb: typing.Optional["base.InputFile"] = None
    stickers: typing.Optional[list["base.InputDocument"]] = None
    ttl_seconds: typing.Optional[int] = None
