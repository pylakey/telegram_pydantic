from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputWebFileAudioAlbumThumbLocation(BaseModel):
    """
    types.InputWebFileAudioAlbumThumbLocation
    ID: 0xf46fe924
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputWebFileAudioAlbumThumbLocation', 'InputWebFileAudioAlbumThumbLocation'] = pydantic.Field(
        'types.InputWebFileAudioAlbumThumbLocation',
        alias='_'
    )

    small: typing.Optional[bool] = None
    document: typing.Optional["base.InputDocument"] = None
    title: typing.Optional[str] = None
    performer: typing.Optional[str] = None
