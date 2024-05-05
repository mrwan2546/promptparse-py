from .parse import Parser
from .model.slipVerify import SlipVerify as SlipVerifyClass


def slipVerify(payload: str):
    ppqr = Parser.parse(payload=payload)
    if not ppqr:
        return None

    apiType = ppqr.getTagValue("00", "00")
    sendingBank = ppqr.getTagValue("00", "01")
    transRef = ppqr.getTagValue("00", "02")

    if apiType != "000001" or not sendingBank or not transRef:
        return None

    return SlipVerifyClass(sendingBank=sendingBank, transRef=transRef)
