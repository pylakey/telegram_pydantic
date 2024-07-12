from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TermsOfServiceUpdate(BaseModel):
    """
    types.help.TermsOfServiceUpdate
    ID: 0x28ecf961
    Layer: 181
    """
    QUALNAME: typing.Literal['types.help.TermsOfServiceUpdate', 'TermsOfServiceUpdate'] = pydantic.Field(
        'types.help.TermsOfServiceUpdate',
        alias='_'
    )

    expires: Datetime
    terms_of_service: "base.help.TermsOfService"
