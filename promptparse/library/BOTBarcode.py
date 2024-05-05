from typing import Self

from ..generator.billpayment import billPayment


class BOTBarcode:
    billerId: str
    ref1: str
    ref2: str
    amount: int

    def __init__(
        self, billterId: str, ref1: str, amount: int = 0, ref2: str = ""
    ) -> None:
        self.billerId = billterId
        self.ref1 = ref1
        self.ref2 = ref2
        self.amount = amount

    @staticmethod
    def fromString(payload: str) -> Self:
        if not payload.startswith("|"):
            return None

        data = payload[1:].split("\r")[0:4]
        return BOTBarcode(
            billterId=data[0],
            ref1=data[1],
            ref2=data[2] if len(data[2]) > 0 else None,
            amount=round(float(data[3]), 2) if data[3] else 0,
        )

    def toString(self):
        if self.amount != 0:
            self.amount = round(self.amount, 2)

        return f"|{self.billerId}\r{self.ref1}\r{self.ref2}\r{self.amount}"

    def toQrTag30(self):
        return billPayment(
            billterId=self.billerId, ref1=self.ref1, ref2=self.ref2, amount=self.amount
        )
