import varint
from bitswap.varint_decoder import varint_decoder


def test_varint_decoder():
    buffer = b""
    numbers = [12, 5168, 4984531, 151]
    for n in numbers:
        buffer += varint.encode(n)
    ans = varint_decoder(buffer)
    assert ans == numbers
