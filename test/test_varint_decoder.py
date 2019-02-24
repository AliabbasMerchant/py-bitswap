import varint
import unittest
from bitswap.varint_decoder import varint_decoder


class VarintDecoderTest(unittest.TestCase):
    def test_varint_decoder(self):
        buffer = b""
        numbers = [12, 5168, 4984531, 151]
        for n in numbers:
            buffer += varint.encode(n)
        ans = varint_decoder(buffer)
        self.assertEqual(ans, numbers)


if __name__ == '__main__':
    unittest.main()
