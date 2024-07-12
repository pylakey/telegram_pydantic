from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UploadWallPaper(BaseModel):
    """
    functions.account.UploadWallPaper
    ID: 0xe39a8f03
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.UploadWallPaper', 'UploadWallPaper'] = pydantic.Field(
        'functions.account.UploadWallPaper',
        alias='_'
    )

    file: "base.InputFile"
    mime_type: str
    settings: "base.WallPaperSettings"
    for_chat: typing.Optional[bool] = None
