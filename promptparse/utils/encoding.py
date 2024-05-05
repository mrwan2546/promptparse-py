def encodeTag81(message: str):
    result = ""
    for string in list(map(str, message)):
        result += str(hex(ord(string)))[2:].rjust(4, "0").upper()
    return result
