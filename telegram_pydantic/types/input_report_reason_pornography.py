from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputReportReasonPornography(BaseModel):
    """
    types.InputReportReasonPornography
    ID: 0x2e59d922
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputReportReasonPornography', 'InputReportReasonPornography'] = pydantic.Field(
        'types.InputReportReasonPornography',
        alias='_'
    )

