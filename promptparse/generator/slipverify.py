from ..library.tlv import TLV


def slipVerify(sendingBank: str, transRef: str):
    payload = [
        TLV.tag(
            "00",
            TLV.encode(
                [
                    TLV.tag("00", "000001"),
                    TLV.tag("01", sendingBank),
                    TLV.tag("02", transRef),
                ]
            ),
        ),
        TLV.tag("51", "TH"),
    ]

    return TLV.withCRCTag(TLV.encode(payload))


def truemoneySlipVerify(eventType: str, transactionId: str, transferDate: str):
    payload = [
        TLV.tag(
            "00",
            TLV.encode(
                [
                    TLV.tag("00", "01"),
                    TLV.tag("01", "01"),
                    TLV.tag("02", eventType),
                    TLV.tag("03", transactionId),
                    TLV.tag("04", transferDate),
                ]
            ),
        ),
    ]

    return TLV.withCRCTag(TLV.encode(payload))
