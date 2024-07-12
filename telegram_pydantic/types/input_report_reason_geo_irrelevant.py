from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputReportReasonGeoIrrelevant(BaseModel):
    """
    types.InputReportReasonGeoIrrelevant
    ID: 0xdbd4feed
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputReportReasonGeoIrrelevant', 'InputReportReasonGeoIrrelevant'] = pydantic.Field(
        'types.InputReportReasonGeoIrrelevant',
        alias='_'
    )

