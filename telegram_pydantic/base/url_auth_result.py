from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# UrlAuthResult - Layer 181
UrlAuthResult = typing.Annotated[
    typing.Union[
        typing.Annotated[types.UrlAuthResultAccepted, pydantic.Tag('UrlAuthResultAccepted')],
        typing.Annotated[types.UrlAuthResultDefault, pydantic.Tag('UrlAuthResultDefault')],
        typing.Annotated[types.UrlAuthResultRequest, pydantic.Tag('UrlAuthResultRequest')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
