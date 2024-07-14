from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# help.PassportConfig - Layer 181
PassportConfig = typing.Annotated[
    typing.Union[
        typing.Annotated[
            types.help.PassportConfig,
            pydantic.Tag('help.PassportConfig'),
            pydantic.Tag('PassportConfig')
        ],
        typing.Annotated[
            types.help.PassportConfigNotModified,
            pydantic.Tag('help.PassportConfigNotModified'),
            pydantic.Tag('PassportConfigNotModified')
        ]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
