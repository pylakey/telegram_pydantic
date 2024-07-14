from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# account.EmailVerified - Layer 181
EmailVerified = typing.Annotated[
    typing.Union[
        typing.Annotated[
            types.account.EmailVerified,
            pydantic.Tag('account.EmailVerified'),
            pydantic.Tag('EmailVerified')
        ],
        typing.Annotated[
            types.account.EmailVerifiedLogin,
            pydantic.Tag('account.EmailVerifiedLogin'),
            pydantic.Tag('EmailVerifiedLogin')
        ]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
