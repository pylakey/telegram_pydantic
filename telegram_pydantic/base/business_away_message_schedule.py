from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# BusinessAwayMessageSchedule - Layer 181
BusinessAwayMessageSchedule = typing.Annotated[
    typing.Union[
        typing.Annotated[types.BusinessAwayMessageScheduleAlways, pydantic.Tag('BusinessAwayMessageScheduleAlways')],
        typing.Annotated[types.BusinessAwayMessageScheduleCustom, pydantic.Tag('BusinessAwayMessageScheduleCustom')],
        typing.Annotated[types.BusinessAwayMessageScheduleOutsideWorkHours, pydantic.Tag('BusinessAwayMessageScheduleOutsideWorkHours')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
