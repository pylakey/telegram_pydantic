from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AcceptTermsOfService(BaseModel):
    """
    functions.help.AcceptTermsOfService
    ID: 0xee72f79a
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.help.AcceptTermsOfService', 'AcceptTermsOfService'] = pydantic.Field(
        'functions.help.AcceptTermsOfService',
        alias='_'
    )

    id: "base.DataJSON"
