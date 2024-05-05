class SlipVerify(object):
    sendingBank: str
    transRef: str

    def __init__(self, sendingBank: str, transRef: str) -> None:
        self.sendingBank = sendingBank
        self.transRef = transRef
