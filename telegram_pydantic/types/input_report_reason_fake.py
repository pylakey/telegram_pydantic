from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputReportReasonFake(BaseModel):
    """
    types.InputReportReasonFake
    ID: 0xf5ddd6e7
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputReportReasonFake', 'InputReportReasonFake'] = pydantic.Field(
        'types.InputReportReasonFake',
        alias='_'
    )

