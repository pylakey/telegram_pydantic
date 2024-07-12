from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SponsoredMessageReportResultChooseOption(BaseModel):
    """
    types.channels.SponsoredMessageReportResultChooseOption
    ID: 0x846f9e42
    Layer: 181
    """
    QUALNAME: typing.Literal['types.channels.SponsoredMessageReportResultChooseOption', 'SponsoredMessageReportResultChooseOption'] = pydantic.Field(
        'types.channels.SponsoredMessageReportResultChooseOption',
        alias='_'
    )

    title: str
    options: list["base.SponsoredMessageReportOption"]
