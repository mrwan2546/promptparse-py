# Promptparse Python

"All-in-one Python for PromptPay & EMVCo QR Codes"

That No dependency required. So there we go!

## Original library from (Forked from)

[maythiwat/promptparse](https://github.com/maythiwat/promptparse)

## Insatallation

```sh
pip3 install git+https://github.com/mrwan200/promptparse-py
```

## Features

- **Parse** &mdash; PromptPay & EMVCo QR Code data strings into object
- **Generate** &mdash; QR Code data from pre-made templates (for example: PromptPay AnyID, PromptPay Bill Payment, TrueMoney, etc.)
- **Manipulate** &mdash; any values from parsed QR Code data (for example: transfer amount, account number) and encodes back into QR Code data
- **Validate** &mdash; checksum and data structure for known QR Code formats (for example: Slip Verify API Mini QR)

## Usage

### Parsing data and get value from tag

```py
from promptparse import Parser

try:
    parsed = Parser.parse("000201010212293....")
    if not parsed:
        print("Parse failed")

    parsed.getTag("00") # Result: 01
except:
    print("Parse failed")
```

### Build QR data and append CRC tag

```py
from promptparse import TLV

payload = [
    TLV.tag("00", "01"),
    TLV.tag("01", "11")
]

TLV.withCRCTag(TLV.encode(payload), "63")
```

### Generate PromptPay Bill Payment QR

```py
from promptparse.generator.billpayment import billpayment

billPayment(billterId="1xxxxxxxxxxxx", amount=300, ref1="INV12345")
```

### Validate & extract data from Slip Verify QR

```py
from promptparse.validate import slipVerify

try:
    result = slipVerify("0041000600....")
    if not result:
        print("Slip validate failed.")
    
    print(result.sendingBank, result.transRef)
except:
    print("Slip validate failed.")
```

### Validate & extract data from Truemoney Slip Verify QR

```py
from promptparse.validate import truemoneySlipVerify

try:
    result = truemoneySlipVerify("0049000....")
    if not result:
        print("Slip validate failed.")
    
    print(result.eventType, result.transactionId, result.transferDate)
except:
    print("Slip validate failed.")
```


### Convert BOT Barcode to PromptPay QR Tag 30 (Bill Payment)

```py
from promptparse import Parser

try:
    parsed = Parser.parseBarcode("|099400016550100\r020020411530\r661229\r111109")
    if not parsed:
        print("Parse failed")

    print(parsed.toQrTag30())
except:
    print("Parse failed")
```

## References

- [EMV QR Code](https://www.emvco.com/emv-technologies/qrcodes/)
- [Thai QR Payment Standard](https://www.bot.or.th/content/dam/bot/fipcs/documents/FPG/2562/ThaiPDF/25620084.pdf)
- [Slip Verify API Mini QR Data](https://developer.scb/assets/documents/documentation/qr-payment/extracting-data-from-mini-qr.pdf)
- [BOT Barcode Standard](https://www.bot.or.th/content/dam/bot/documents/th/our-roles/payment-systems/about-payment-systems/Std_Barcode.pdf)

## See also

- [phoomin2012/promptparse-php](https://github.com/phoomin2012/promptparse-php) PromptParse port for PHP

## License

This project is MIT licensed (see [LICENSE](LICENSE))
