from typing import List, Union

from ..model.tlv import TLVModel
from .tlv import TLV


class EMVCoQR:
    __payload: str = ""
    __tags: List[TLVModel] = []

    def __init__(self, payload: str, tags: List[TLVModel]) -> None:
        self.__payload = payload
        self.__tags = tags

    def getTag(self, tagId: str, subTagId=None) -> Union[TLVModel, None]:
        return TLV.get(self.__tags, tagId, subTagId)

    def getTagValue(self, tagId: str, subTagId=None) -> str:
        return TLV.get(self.__tags, tagId, subTagId).value

    def getTags(self) -> List[TLVModel]:
        return self.__tags

    def getPayload(self) -> str:
        return self.__payload

    def validate(self, crcTagId: str):
        tags = []

        for tag in self.__tags:
            if tag.id != crcTagId:
                tags.append(tag)

        excepted = TLV.withCRCTag(TLV.encode(tags=tags), crcTagId)

        return excepted == self.__payload
