from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# channels.SponsoredMessageReportResult - Layer 181
SponsoredMessageReportResult = typing.Annotated[
    typing.Union[
        typing.Annotated[types.channels.SponsoredMessageReportResultAdsHidden, pydantic.Tag('channels.SponsoredMessageReportResultAdsHidden')],
        typing.Annotated[types.channels.SponsoredMessageReportResultChooseOption, pydantic.Tag('channels.SponsoredMessageReportResultChooseOption')],
        typing.Annotated[types.channels.SponsoredMessageReportResultReported, pydantic.Tag('channels.SponsoredMessageReportResultReported')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
