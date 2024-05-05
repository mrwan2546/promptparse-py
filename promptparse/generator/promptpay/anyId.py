from typing import Union

from ...library.tlv import TLV
from ...model.proxy import ProxyMethod


def anyId(method: Union[ProxyMethod, str], target: str, amount: float = 0) -> str:
    # Check if is proxy class
    if isinstance(method, tuple):
        method = method[0]

    if method == "01":
        if target.startswith("0"):
            target = "66" + target[1:]

        target = target.rjust(13, "0")

    tag29 = [TLV.tag("00", "A000000677010111"), TLV.tag(method, target)]

    payload = [
        TLV.tag("00", "01"),
        TLV.tag("01", "11" if not amount else "12"),
        TLV.tag("29", TLV.encode(tag29)),
        TLV.tag("53", "764"),
        TLV.tag("58", "TH"),
    ]

    if amount:
        payload.append(TLV.tag("54", "{:.2f}".format(amount)))

    return TLV.withCRCTag(TLV.encode(payload), "63")
