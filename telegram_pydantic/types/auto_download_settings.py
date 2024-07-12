from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AutoDownloadSettings(BaseModel):
    """
    types.AutoDownloadSettings
    ID: 0xbaa57628
    Layer: 181
    """
    QUALNAME: typing.Literal['types.AutoDownloadSettings', 'AutoDownloadSettings'] = pydantic.Field(
        'types.AutoDownloadSettings',
        alias='_'
    )

    photo_size_max: int
    video_size_max: int
    file_size_max: int
    video_upload_maxbitrate: int
    small_queue_active_operations_max: int
    large_queue_active_operations_max: int
    disabled: typing.Optional[bool] = None
    video_preload_large: typing.Optional[bool] = None
    audio_preload_next: typing.Optional[bool] = None
    phonecalls_less_data: typing.Optional[bool] = None
    stories_preload: typing.Optional[bool] = None
