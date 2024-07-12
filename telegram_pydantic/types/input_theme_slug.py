from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputThemeSlug(BaseModel):
    """
    types.InputThemeSlug
    ID: 0xf5890df1
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputThemeSlug', 'InputThemeSlug'] = pydantic.Field(
        'types.InputThemeSlug',
        alias='_'
    )

    slug: str
