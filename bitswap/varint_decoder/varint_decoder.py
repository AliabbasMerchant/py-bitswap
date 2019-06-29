import varint
import io
from typing import List


def varint_decoder(buffer: bytes) -> List[int]:
    if not isinstance(buffer, bytes):
        raise TypeError('buffer must be a bytes object, not {}'.format(type(buffer)))
    stream = io.BytesIO(buffer)
    result = []
    while stream.tell() < len(buffer):
        result.append(varint.decode_stream(stream))
    return result
