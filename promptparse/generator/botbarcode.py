from ..library.BOTBarcode import BOTBarcode

def botBarcode(billerId: str, ref1: str, ref2: str, amount: float = 0):
    return BOTBarcode(
        billterId=billerId, ref1=ref1, ref2=ref2, amount=amount
    ).toString()
