from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# help.CountriesList - Layer 181
CountriesList = typing.Annotated[
    typing.Union[
        typing.Annotated[types.help.CountriesList, pydantic.Tag('help.CountriesList')],
        typing.Annotated[types.help.CountriesListNotModified, pydantic.Tag('help.CountriesListNotModified')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
