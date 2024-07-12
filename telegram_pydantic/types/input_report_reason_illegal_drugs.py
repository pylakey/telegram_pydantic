from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputReportReasonIllegalDrugs(BaseModel):
    """
    types.InputReportReasonIllegalDrugs
    ID: 0xa8eb2be
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputReportReasonIllegalDrugs', 'InputReportReasonIllegalDrugs'] = pydantic.Field(
        'types.InputReportReasonIllegalDrugs',
        alias='_'
    )

