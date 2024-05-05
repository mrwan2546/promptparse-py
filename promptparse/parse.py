import re

from .library.tlv import TLV
from .library.EMVCoQR import EMVCoQR
from .library.BOTBarcode import BOTBarcode

REGEX = re.compile(r"^\d{4}.+")


class Parser:
    @staticmethod
    def parse(payload: str, strict=False, sub_tag=True):
        if not REGEX.match(payload):
            return None

        if strict:
            excepted = payload[-3:]
            calculated = TLV.withCRCTag(payload=payload[:-4])
            if excepted != calculated:
                return None

        tags = TLV.decode(payload=payload)

        if sub_tag:
            for idx, tag in enumerate(tags):
                # Check if invalid
                if not REGEX.match(tag.value):
                    continue

                sub = TLV.decode(tag.value)

                for tag in sub:
                    if tag.length == 0 or tag.length != len(tag.value):
                        continue

                tags[idx].sub_tags = sub

        return EMVCoQR(payload=payload, tags=tags)

    @staticmethod
    def parseBarcode(payload: str) -> BOTBarcode:
        return BOTBarcode.fromString(payload=payload)