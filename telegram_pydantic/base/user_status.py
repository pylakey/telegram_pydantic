from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# UserStatus - Layer 181
UserStatus = typing.Annotated[
    typing.Union[
        typing.Annotated[types.UserStatusEmpty, pydantic.Tag('UserStatusEmpty')],
        typing.Annotated[types.UserStatusLastMonth, pydantic.Tag('UserStatusLastMonth')],
        typing.Annotated[types.UserStatusLastWeek, pydantic.Tag('UserStatusLastWeek')],
        typing.Annotated[types.UserStatusOffline, pydantic.Tag('UserStatusOffline')],
        typing.Annotated[types.UserStatusOnline, pydantic.Tag('UserStatusOnline')],
        typing.Annotated[types.UserStatusRecently, pydantic.Tag('UserStatusRecently')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
