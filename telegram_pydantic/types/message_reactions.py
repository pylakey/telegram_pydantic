from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageReactions(BaseModel):
    """
    types.MessageReactions
    ID: 0x4f2b9479
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageReactions', 'MessageReactions'] = pydantic.Field(
        'types.MessageReactions',
        alias='_'
    )

    results: list["base.ReactionCount"]
    min: typing.Optional[bool] = None
    can_see_list: typing.Optional[bool] = None
    reactions_as_tags: typing.Optional[bool] = None
    recent_reactions: typing.Optional[list["base.MessagePeerReaction"]] = None
