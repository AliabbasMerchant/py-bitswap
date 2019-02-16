from bitswap import WantListEntry
from bitswap import MessageEntry
import unittest
import cid as py_cid


class MessageEntryTest(unittest.TestCase):

    def test_init_cid_priority(self):
        cid = py_cid.make_cid('QmaozNR7DZHQK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdT3L4')
        m = MessageEntry(cid, False)
        self.assertEqual(m.entry, WantListEntry(cid))
        self.assertEqual(m.cid, cid)
        self.assertEqual(m.cancel, False)
        self.assertEqual(m.priority, 1)
        m = MessageEntry(cid, True, 5)
        self.assertEqual(m.entry, WantListEntry(cid, 5))
        self.assertEqual(m.cid, cid)
        self.assertEqual(m.cancel, True)
        self.assertEqual(m.priority, 5)
        with self.assertRaises(ValueError):
            MessageEntry('df', True)

    def test_str(self):
        cid = py_cid.make_cid('QmaozNR7DZHQK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdT3L4')
        m = MessageEntry(cid, True, 5)
        expected = f'BitswapMessageEntry (cid={str(cid)}, priority=5, cancel=True)'
        self.assertEqual(expected, str(m))

    def test_eq(self):
        cid = py_cid.make_cid('QmaozNR7DZHQK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdT3L4')
        m = MessageEntry(cid, True, 5)
        m2 = MessageEntry(cid, True, 5)
        self.assertTrue(m.equals(m2))
        self.assertTrue(m == m2)
        m2.cancel = False
        self.assertFalse(m.equals(m2))  # different cancel
        self.assertFalse(m == m2)  # different cancel
        cid2 = py_cid.make_cid('QmaozNR7DZHQK1ZcU9p7QdrshMvXqW71ZcU9p7QdrshMpa')
        m2 = MessageEntry(cid2, True, 5)
        self.assertFalse(m.equals(m2))  # different cid
        self.assertFalse(m == m2)  # different cid


if __name__ == '__main__':
    unittest.main()
