from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# ReactionNotificationsFrom - Layer 181
ReactionNotificationsFrom = typing.Annotated[
    typing.Union[
        typing.Annotated[types.ReactionNotificationsFromAll, pydantic.Tag('ReactionNotificationsFromAll')],
        typing.Annotated[types.ReactionNotificationsFromContacts, pydantic.Tag('ReactionNotificationsFromContacts')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
