from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# auth.SentCodeType - Layer 181
SentCodeType = typing.Annotated[
    typing.Union[
        typing.Annotated[
            types.auth.SentCodeTypeApp,
            pydantic.Tag('auth.SentCodeTypeApp'),
            pydantic.Tag('SentCodeTypeApp')
        ],
        typing.Annotated[
            types.auth.SentCodeTypeCall,
            pydantic.Tag('auth.SentCodeTypeCall'),
            pydantic.Tag('SentCodeTypeCall')
        ],
        typing.Annotated[
            types.auth.SentCodeTypeEmailCode,
            pydantic.Tag('auth.SentCodeTypeEmailCode'),
            pydantic.Tag('SentCodeTypeEmailCode')
        ],
        typing.Annotated[
            types.auth.SentCodeTypeFirebaseSms,
            pydantic.Tag('auth.SentCodeTypeFirebaseSms'),
            pydantic.Tag('SentCodeTypeFirebaseSms')
        ],
        typing.Annotated[
            types.auth.SentCodeTypeFlashCall,
            pydantic.Tag('auth.SentCodeTypeFlashCall'),
            pydantic.Tag('SentCodeTypeFlashCall')
        ],
        typing.Annotated[
            types.auth.SentCodeTypeFragmentSms,
            pydantic.Tag('auth.SentCodeTypeFragmentSms'),
            pydantic.Tag('SentCodeTypeFragmentSms')
        ],
        typing.Annotated[
            types.auth.SentCodeTypeMissedCall,
            pydantic.Tag('auth.SentCodeTypeMissedCall'),
            pydantic.Tag('SentCodeTypeMissedCall')
        ],
        typing.Annotated[
            types.auth.SentCodeTypeSetUpEmailRequired,
            pydantic.Tag('auth.SentCodeTypeSetUpEmailRequired'),
            pydantic.Tag('SentCodeTypeSetUpEmailRequired')
        ],
        typing.Annotated[
            types.auth.SentCodeTypeSms,
            pydantic.Tag('auth.SentCodeTypeSms'),
            pydantic.Tag('SentCodeTypeSms')
        ],
        typing.Annotated[
            types.auth.SentCodeTypeSmsPhrase,
            pydantic.Tag('auth.SentCodeTypeSmsPhrase'),
            pydantic.Tag('SentCodeTypeSmsPhrase')
        ],
        typing.Annotated[
            types.auth.SentCodeTypeSmsWord,
            pydantic.Tag('auth.SentCodeTypeSmsWord'),
            pydantic.Tag('SentCodeTypeSmsWord')
        ]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
