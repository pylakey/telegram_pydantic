from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StatsGraph(BaseModel):
    """
    types.StatsGraph
    ID: 0x8ea464b6
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StatsGraph', 'StatsGraph'] = pydantic.Field(
        'types.StatsGraph',
        alias='_'
    )

    json_: "base.DataJSON" = pydantic.Field(
        ...,
        serialization_alias='json',
        validation_alias=pydantic.AliasChoices('json', 'json_')
    )
    zoom_token: typing.Optional[str] = None
