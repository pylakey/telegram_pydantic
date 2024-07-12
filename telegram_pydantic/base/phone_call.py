from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# PhoneCall - Layer 181
PhoneCall = typing.Annotated[
    typing.Union[
        typing.Annotated[types.PhoneCall, pydantic.Tag('PhoneCall')],
        typing.Annotated[types.PhoneCallAccepted, pydantic.Tag('PhoneCallAccepted')],
        typing.Annotated[types.PhoneCallDiscarded, pydantic.Tag('PhoneCallDiscarded')],
        typing.Annotated[types.PhoneCallEmpty, pydantic.Tag('PhoneCallEmpty')],
        typing.Annotated[types.PhoneCallRequested, pydantic.Tag('PhoneCallRequested')],
        typing.Annotated[types.PhoneCallWaiting, pydantic.Tag('PhoneCallWaiting')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
