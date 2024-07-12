from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GroupCallParticipantVideoSourceGroup(BaseModel):
    """
    types.GroupCallParticipantVideoSourceGroup
    ID: 0xdcb118b7
    Layer: 181
    """
    QUALNAME: typing.Literal['types.GroupCallParticipantVideoSourceGroup', 'GroupCallParticipantVideoSourceGroup'] = pydantic.Field(
        'types.GroupCallParticipantVideoSourceGroup',
        alias='_'
    )

    semantics: str
    sources: list[int]
