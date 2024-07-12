from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ExportStoryLink(BaseModel):
    """
    functions.stories.ExportStoryLink
    ID: 0x7b8def20
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stories.ExportStoryLink', 'ExportStoryLink'] = pydantic.Field(
        'functions.stories.ExportStoryLink',
        alias='_'
    )

    peer: "base.InputPeer"
    id: int
