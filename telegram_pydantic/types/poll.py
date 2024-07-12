from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Poll(BaseModel):
    """
    types.Poll
    ID: 0x58747131
    Layer: 181
    """
    QUALNAME: typing.Literal['types.Poll', 'Poll'] = pydantic.Field(
        'types.Poll',
        alias='_'
    )

    id: int
    question: "base.TextWithEntities"
    answers: list["base.PollAnswer"]
    closed: typing.Optional[bool] = None
    public_voters: typing.Optional[bool] = None
    multiple_choice: typing.Optional[bool] = None
    quiz: typing.Optional[bool] = None
    close_period: typing.Optional[int] = None
    close_date: Datetime
