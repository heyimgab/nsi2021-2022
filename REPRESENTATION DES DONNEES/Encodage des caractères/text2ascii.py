from typing import List

msg=str(input('Entrez le mot à convertir en ascii:'))

def encode(msg: str):
    code: List[int] = [ord(c) for c in msg]
    return code

def decode(code: List[int]):
    decoded: List[str] = [chr(element) for element in code]
    output: str = "".join(decoded)
    return output