from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# help.TimezonesList - Layer 181
TimezonesList = typing.Annotated[
    typing.Union[
        typing.Annotated[types.help.TimezonesList, pydantic.Tag('help.TimezonesList')],
        typing.Annotated[types.help.TimezonesListNotModified, pydantic.Tag('help.TimezonesListNotModified')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
