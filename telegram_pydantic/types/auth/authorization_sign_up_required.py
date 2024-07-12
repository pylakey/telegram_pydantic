from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AuthorizationSignUpRequired(BaseModel):
    """
    types.auth.AuthorizationSignUpRequired
    ID: 0x44747e9a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.auth.AuthorizationSignUpRequired', 'AuthorizationSignUpRequired'] = pydantic.Field(
        'types.auth.AuthorizationSignUpRequired',
        alias='_'
    )

    terms_of_service: typing.Optional["base.help.TermsOfService"] = None
