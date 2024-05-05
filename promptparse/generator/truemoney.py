from ..library.tlv import TLV
from ..utils.encoding import encodeTag81


def truemoney(mobileNo: str, amount: float, message: str = ""):
    tag29 = [TLV.tag("00", "A000000677010111"), TLV.tag("03", "14000" + mobileNo)]

    payload = [
        TLV.tag("00", "01"),
        TLV.tag("01", "11" if not amount else "12"),
        TLV.tag("29", TLV.encode(tag29)),
        TLV.tag("53", "764"),
        TLV.tag("58", "TH"),
    ]

    if amount:
        payload.append(TLV.tag("54", "{:.2f}".format(amount)))

    if message:
        payload.append(TLV.tag("81", encodeTag81(message=message)))

    return TLV.withCRCTag(TLV.encode(payload), "63")
