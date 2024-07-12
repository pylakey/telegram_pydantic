from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateGroupCallParticipants(BaseModel):
    """
    types.UpdateGroupCallParticipants
    ID: 0xf2ebdb4e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateGroupCallParticipants', 'UpdateGroupCallParticipants'] = pydantic.Field(
        'types.UpdateGroupCallParticipants',
        alias='_'
    )

    call: "base.InputGroupCall"
    participants: list["base.GroupCallParticipant"]
    version: int
