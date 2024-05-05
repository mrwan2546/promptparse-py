from ..library.tlv import TLV


def billPayment(billterId: str, ref1: str, ref2: str = "", ref3: str = "", amount: float = 0):
    tag30 = [
        TLV.tag("00", "A000000677010112"),
        TLV.tag("01", billterId),
        TLV.tag("02", ref1),
    ]

    if ref2:
        tag30.append(TLV.tag("03", ref2))

    payload = [
        TLV.tag("00", "01"),
        TLV.tag("01", "11" if not amount else "12"),
        TLV.tag("30", TLV.encode(tag30)),
        TLV.tag("53", "764"),
        TLV.tag("58", "TH"),
    ]

    if amount:
        payload.append(TLV.tag("54", "{:.2f}".format(amount)))

    if ref3:
        payload.append(TLV.tag("62", ref3))

    return TLV.withCRCTag(TLV.encode(payload), "63")
