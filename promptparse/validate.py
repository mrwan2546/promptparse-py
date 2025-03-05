from .parse import Parser
from .model.slipVerify import (
    SlipVerify as SlipVerifyClass,
    TruemoneySlipVerify as TruemoneySlipVerifyClass,
)


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


def truemoneySlipVerify(payload: str):
    ppqr = Parser.parse(payload=payload)
    if not ppqr:
        return None

    validation1 = ppqr.getTagValue("00", "00")
    validation2 = ppqr.getTagValue("00", "01")

    eventType = ppqr.getTagValue("00", "02")
    transactionId = ppqr.getTagValue("00", "03")
    transferDate = ppqr.getTagValue("00", "04")

    if validation1 != "01" and validation2 != "01":
        return None

    return TruemoneySlipVerifyClass(
        eventType=eventType, transactionId=transactionId, transferDate=transferDate
    )
