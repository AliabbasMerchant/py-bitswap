from bitswap import BitswapMessage
import unittest
import cid as py_cid


class MessageEntryTest(unittest.TestCase):

    def setUp(self):
        self.bm = BitswapMessage(False)

    def test_empty(self):
        pass

    def test_add_entry(self):
        cid = py_cid.make_cid('QmaozNR7DZHQK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdT3L4')
        cid_str = str(cid)
        with self.assertRaises(ValueError):
            self.bm.add_entry('df', True)

    def test_add_block(self):
        pass

    def test_cancel(self):
        pass

    def test_equals(self):
        pass

    def test_serialize_to_bitswap_100(self):
        pass

    def test_serialize_to_bitswap_110(self):
        pass

    def test_deserialize(self):
        pass

    def test_str(self):
        pass


if __name__ == '__main__':
    unittest.main()
