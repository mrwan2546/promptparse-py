class SlipVerify(object):
    sendingBank: str
    transRef: str

    def __init__(self, sendingBank: str, transRef: str) -> None:
        self.sendingBank = sendingBank
        self.transRef = transRef

class TruemoneySlipVerify(object):
    eventType: str
    transactionId: str
    transferDate: str

    def __init__(self, eventType: str, transactionId: str, transferDate: str) -> None:
        self.eventType = eventType
        self.transactionId = transactionId
        self.transferDate = transferDate
