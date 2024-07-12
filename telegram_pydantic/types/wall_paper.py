from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class WallPaper(BaseModel):
    """
    types.WallPaper
    ID: 0xa437c3ed
    Layer: 181
    """
    QUALNAME: typing.Literal['types.WallPaper', 'WallPaper'] = pydantic.Field(
        'types.WallPaper',
        alias='_'
    )

    id: int
    access_hash: int
    slug: str
    document: "base.Document"
    creator: typing.Optional[bool] = None
    default: typing.Optional[bool] = None
    pattern: typing.Optional[bool] = None
    dark: typing.Optional[bool] = None
    settings: typing.Optional["base.WallPaperSettings"] = None
