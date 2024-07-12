from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AutoSaveSettings(BaseModel):
    """
    types.AutoSaveSettings
    ID: 0xc84834ce
    Layer: 181
    """
    QUALNAME: typing.Literal['types.AutoSaveSettings', 'AutoSaveSettings'] = pydantic.Field(
        'types.AutoSaveSettings',
        alias='_'
    )

    photos: typing.Optional[bool] = None
    videos: typing.Optional[bool] = None
    video_max_size: typing.Optional[int] = None
