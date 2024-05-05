from typing import List, Union, Self

from ..model.tlv import TLVModel
from ..utils.crc16 import CRC16XModem


class TLV(TLVModel):
    def __init__(
        self,
        id: str,
        length: int,
        value: str,
        sub_tags: List[TLVModel],
    ) -> None:
        self.id = id
        self.value = value
        self.length = length
        self.sub_tags = sub_tags

    @staticmethod
    def encode(tags: List[TLVModel]) -> str:
        payload = ""

        for tag in tags:
            payload += tag.id
            payload += str(tag.length).rjust(2, "0")
            if len(tag.sub_tags) > 0:
                payload += TLV.encode(tags=tag.sub_tags)
            else:
                payload += tag.value

        return payload

    @staticmethod
    def decode(payload: str) -> List[TLVModel]:
        index = 0
        tags = []

        while index < len(payload):
            data = payload[index:]
            _id = data[0:2]
            _length = int(data[2:4])
            _value = data[4 : 4 + _length]
            tags.append(TLV(_id, _length, _value, []))

            index += _length + 4

        return tags

    @staticmethod
    def checksum(payload: str) -> str:
        return str(CRC16XModem(0xFFFF).update(payload).pack())[2:].upper()

    @staticmethod
    def withCRCTag(payload: str, crcTagId: str) -> str:
        payload += crcTagId.rjust(2, "0")
        payload += "04"
        payload += TLV.checksum(payload)
        return payload

    @staticmethod
    def get(tlvTag: List[TLVModel], tagId: str, subTagId=None) -> Union[TLVModel, None]:
        tagInfo = None

        for tag in tlvTag:
            if tag.id == tagId:
                tagInfo = tag
        if subTagId is not None:
            for subTag in tagInfo.sub_tags:
                if subTag.id == subTagId:
                    return subTag

        return tagInfo

    @staticmethod
    def tag(tagId: str, value: str) -> TLVModel:
        return TLV(id=tagId, length=len(value), value=value, sub_tags=[])
