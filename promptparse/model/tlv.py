from abc import ABC
from typing import List


class TLVBase(ABC):
    id: str
    value: str
    length: int


class TLVWitSubTag(TLVBase):
    sub_tags: List[TLVBase]

class TLVModel(TLVWitSubTag):
    ...