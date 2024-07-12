from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetStoryReactionsList(BaseModel):
    """
    functions.stories.GetStoryReactionsList
    ID: 0xb9b2881f
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stories.GetStoryReactionsList', 'GetStoryReactionsList'] = pydantic.Field(
        'functions.stories.GetStoryReactionsList',
        alias='_'
    )

    peer: "base.InputPeer"
    id: int
    limit: int
    forwards_first: typing.Optional[bool] = None
    reaction: typing.Optional["base.Reaction"] = None
    offset: typing.Optional[str] = None
