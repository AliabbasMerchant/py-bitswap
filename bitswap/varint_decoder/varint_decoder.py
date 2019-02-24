import varint
from typing import List


def varint_decoder(buffer: bytes) -> List[int]:
    if not isinstance(buffer, bytes):
        raise TypeError('buffer must be a bytes object, not {}'.format(type(buffer)))
    result = []
    while len(buffer) > 0:
        num = varint.decode_bytes(buffer)
        result.append(num)
        buffer = buffer[len(varint.encode(num)):]
    return result
