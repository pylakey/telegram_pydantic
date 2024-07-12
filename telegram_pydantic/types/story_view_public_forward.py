from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StoryViewPublicForward(BaseModel):
    """
    types.StoryViewPublicForward
    ID: 0x9083670b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StoryViewPublicForward', 'StoryViewPublicForward'] = pydantic.Field(
        'types.StoryViewPublicForward',
        alias='_'
    )

    message: "base.Message"
    blocked: typing.Optional[bool] = None
    blocked_my_stories_from: typing.Optional[bool] = None
