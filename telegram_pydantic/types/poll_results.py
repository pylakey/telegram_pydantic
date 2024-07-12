from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PollResults(BaseModel):
    """
    types.PollResults
    ID: 0x7adf2420
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PollResults', 'PollResults'] = pydantic.Field(
        'types.PollResults',
        alias='_'
    )

    min: typing.Optional[bool] = None
    results: typing.Optional[list["base.PollAnswerVoters"]] = None
    total_voters: typing.Optional[int] = None
    recent_voters: typing.Optional[list["base.Peer"]] = None
    solution: typing.Optional[str] = None
    solution_entities: typing.Optional[list["base.MessageEntity"]] = None
