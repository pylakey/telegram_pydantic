from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TermsOfServiceUpdateEmpty(BaseModel):
    """
    types.help.TermsOfServiceUpdateEmpty
    ID: 0xe3309f7f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.help.TermsOfServiceUpdateEmpty', 'TermsOfServiceUpdateEmpty'] = pydantic.Field(
        'types.help.TermsOfServiceUpdateEmpty',
        alias='_'
    )

    expires: Datetime
