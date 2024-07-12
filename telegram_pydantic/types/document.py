from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Document(BaseModel):
    """
    types.Document
    ID: 0x8fd4c4d8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.Document', 'Document'] = pydantic.Field(
        'types.Document',
        alias='_'
    )

    id: int
    access_hash: int
    file_reference: Bytes
    date: Datetime
    mime_type: str
    size: int
    dc_id: int
    attributes: list["base.DocumentAttribute"]
    thumbs: typing.Optional[list["base.PhotoSize"]] = None
    video_thumbs: typing.Optional[list["base.VideoSize"]] = None
