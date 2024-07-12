from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AllStoriesNotModified(BaseModel):
    """
    types.stories.AllStoriesNotModified
    ID: 0x1158fe3e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.stories.AllStoriesNotModified', 'AllStoriesNotModified'] = pydantic.Field(
        'types.stories.AllStoriesNotModified',
        alias='_'
    )

    state: str
    stealth_mode: "base.StoriesStealthMode"
