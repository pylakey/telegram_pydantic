from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# account.WallPapers - Layer 181
WallPapers = typing.Annotated[
    typing.Union[
        typing.Annotated[
            types.account.WallPapers,
            pydantic.Tag('account.WallPapers'),
            pydantic.Tag('WallPapers')
        ],
        typing.Annotated[
            types.account.WallPapersNotModified,
            pydantic.Tag('account.WallPapersNotModified'),
            pydantic.Tag('WallPapersNotModified')
        ]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
