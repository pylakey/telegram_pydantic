from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# help.DeepLinkInfo - Layer 181
DeepLinkInfo = typing.Annotated[
    typing.Union[
        typing.Annotated[types.help.DeepLinkInfo, pydantic.Tag('help.DeepLinkInfo')],
        typing.Annotated[types.help.DeepLinkInfoEmpty, pydantic.Tag('help.DeepLinkInfoEmpty')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
