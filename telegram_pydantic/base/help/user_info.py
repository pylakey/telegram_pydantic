from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# help.UserInfo - Layer 181
UserInfo = typing.Annotated[
    typing.Union[
        typing.Annotated[types.help.UserInfo, pydantic.Tag('help.UserInfo')],
        typing.Annotated[types.help.UserInfoEmpty, pydantic.Tag('help.UserInfoEmpty')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
