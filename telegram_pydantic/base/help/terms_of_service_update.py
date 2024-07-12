from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# help.TermsOfServiceUpdate - Layer 181
TermsOfServiceUpdate = typing.Annotated[
    typing.Union[
        typing.Annotated[types.help.TermsOfServiceUpdate, pydantic.Tag('help.TermsOfServiceUpdate')],
        typing.Annotated[types.help.TermsOfServiceUpdateEmpty, pydantic.Tag('help.TermsOfServiceUpdateEmpty')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
