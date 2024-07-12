from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReportReaction(BaseModel):
    """
    functions.messages.ReportReaction
    ID: 0x3f64c076
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.ReportReaction', 'ReportReaction'] = pydantic.Field(
        'functions.messages.ReportReaction',
        alias='_'
    )

    peer: "base.InputPeer"
    id: int
    reaction_peer: "base.InputPeer"
