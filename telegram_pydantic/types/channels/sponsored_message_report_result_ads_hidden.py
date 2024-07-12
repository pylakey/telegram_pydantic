from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SponsoredMessageReportResultAdsHidden(BaseModel):
    """
    types.channels.SponsoredMessageReportResultAdsHidden
    ID: 0x3e3bcf2f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.channels.SponsoredMessageReportResultAdsHidden', 'SponsoredMessageReportResultAdsHidden'] = pydantic.Field(
        'types.channels.SponsoredMessageReportResultAdsHidden',
        alias='_'
    )

