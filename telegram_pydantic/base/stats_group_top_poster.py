from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# StatsGroupTopPoster - Layer 181
# NOTICE: This is a workaround for pydantic. Discriminated unions doesn't work with single type in Union
# pydantic.Discriminator(base_type_discriminator)
StatsGroupTopPoster = typing.Union[
    typing.Annotated[types.StatsGroupTopPoster, pydantic.Tag('StatsGroupTopPoster')]
]
