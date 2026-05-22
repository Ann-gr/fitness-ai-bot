from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")

@dataclass
class Result(Generic[T]):
    success: bool
    data: T | None = None
    error: str | None = None