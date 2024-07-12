import base64
import typing
from datetime import datetime

import pydantic


def _serialize_bytes(v: bytes) -> str:
    return base64.b64encode(v).decode('ascii')


def _validate_bytes(v: bytes) -> bytes:
    if isinstance(v, bytes):
        return v

    if isinstance(v, str):
        try:
            return base64.b64decode(v.encode('ascii'))
        except Exception as e:
            raise ValueError(f"Invalid base64-encoded bytes: {e}")

    return v


Bytes = typing.Annotated[
    bytes,
    pydantic.PlainSerializer(_serialize_bytes, return_type=str, when_used="json-unless-none"),
    pydantic.BeforeValidator(_validate_bytes),
]


def _serialize_datetime(v: datetime) -> int:
    return int(v.timestamp())


def _validate_datetime(v: datetime) -> datetime:
    if isinstance(v, datetime):
        return v

    if isinstance(v, (int, float)):
        return datetime.fromtimestamp(v)

    if isinstance(v, str):
        try:
            return datetime.fromisoformat(v)
        except Exception:
            pass

        try:
            return datetime.fromtimestamp(int(v))
        except Exception:
            pass

    raise ValueError(f"Invalid datetime value: {v}")


Datetime = typing.Annotated[
    datetime,
    pydantic.PlainSerializer(_serialize_datetime, return_type=int, when_used="json-unless-none"),
    pydantic.BeforeValidator(_validate_datetime),
]
