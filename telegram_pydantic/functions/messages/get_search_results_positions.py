from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetSearchResultsPositions(BaseModel):
    """
    functions.messages.GetSearchResultsPositions
    ID: 0x9c7f2f10
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetSearchResultsPositions', 'GetSearchResultsPositions'] = pydantic.Field(
        'functions.messages.GetSearchResultsPositions',
        alias='_'
    )

    peer: "base.InputPeer"
    filter: "base.MessagesFilter"
    offset_id: int
    limit: int
    saved_peer_id: typing.Optional["base.InputPeer"] = None
