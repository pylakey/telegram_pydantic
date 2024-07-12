from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# ReportReason - Layer 181
ReportReason = typing.Annotated[
    typing.Union[
        typing.Annotated[types.InputReportReasonChildAbuse, pydantic.Tag('InputReportReasonChildAbuse')],
        typing.Annotated[types.InputReportReasonCopyright, pydantic.Tag('InputReportReasonCopyright')],
        typing.Annotated[types.InputReportReasonFake, pydantic.Tag('InputReportReasonFake')],
        typing.Annotated[types.InputReportReasonGeoIrrelevant, pydantic.Tag('InputReportReasonGeoIrrelevant')],
        typing.Annotated[types.InputReportReasonIllegalDrugs, pydantic.Tag('InputReportReasonIllegalDrugs')],
        typing.Annotated[types.InputReportReasonOther, pydantic.Tag('InputReportReasonOther')],
        typing.Annotated[types.InputReportReasonPersonalDetails, pydantic.Tag('InputReportReasonPersonalDetails')],
        typing.Annotated[types.InputReportReasonPornography, pydantic.Tag('InputReportReasonPornography')],
        typing.Annotated[types.InputReportReasonSpam, pydantic.Tag('InputReportReasonSpam')],
        typing.Annotated[types.InputReportReasonViolence, pydantic.Tag('InputReportReasonViolence')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
