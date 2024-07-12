from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StoryReactionPublicForward(BaseModel):
    """
    types.StoryReactionPublicForward
    ID: 0xbbab2643
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StoryReactionPublicForward', 'StoryReactionPublicForward'] = pydantic.Field(
        'types.StoryReactionPublicForward',
        alias='_'
    )

    message: "base.Message"
