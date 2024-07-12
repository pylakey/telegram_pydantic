from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# SearchResultsCalendarPeriod - Layer 181
# NOTICE: This is a workaround for pydantic. Discriminated unions doesn't work with single type in Union
# pydantic.Discriminator(base_type_discriminator)
SearchResultsCalendarPeriod = typing.Union[
    typing.Annotated[types.SearchResultsCalendarPeriod, pydantic.Tag('SearchResultsCalendarPeriod')]
]
