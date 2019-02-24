import unittest
import multihash
from bitswap import multihashing
from Crypto.Hash import SHA1


class MultihashingTest(unittest.TestCase):
    def setUp(self):
        self.functions = {
            'sha1': SHA1
        }
        self.data = b"HelloMultihashing@%4&^&6543"

    def test_create_hash(self):
        for func in self.functions:
            h1 = multihashing.create_hash(func)
            h2 = self.functions[func].new()
            self.assertEqual(str(h1)[:str(h1).rindex("at")], str(h2)[:str(h2).rindex("at")])

    def test_digest(self):
        encoded = multihashing.digest(self.data, 'sha1', 12)
        self.assertEqual(len(encoded), 12)

    def test_multihashing(self):
        for func in self.functions:
            h = self.functions[func].new()
            h.update(self.data)
            d = h.digest()
            ideal = multihash.encode(d, func)
            got = multihashing.multihashing(self.data, func)
            self.assertEqual(ideal, got)
            ideal = multihash.encode(d[:10], func, 10)
            got = multihashing.multihashing(self.data, func, 10)
            self.assertEqual(ideal, got)

    def test_verify(self):
        for func in self.functions:
            h = self.functions[func].new()
            h.update(self.data)
            d = h.digest()
            ideal = multihash.encode(d, func)
            self.assertTrue(multihashing.verify(ideal, self.data))

    def test_validity(self):
        expected = {
            'sha1': "11 14 22 67 fb 69 f1 e1 7f 15 58 83 c2 fa df 22 71 95 7d df 96 62".replace(" ", ""),
            'sha2-256':
                "12 20 91 3d b4 c7 62 ba 95 d7 6c a2 55 9d 04 9d 2c 84 54 a0 11 a6 a4 b8 58 5c 12 ba 74 b5 b8 e9 b1 ab".
                    replace(" ", ""),
        }
        for func in expected:
            self.assertEqual(expected[func], multihashing.multihashing(self.data, func).hex())


if __name__ == '__main__':
    unittest.main()
