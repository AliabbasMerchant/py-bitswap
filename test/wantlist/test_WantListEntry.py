from bitswap import WantListEntry
import unittest
import cid as py_cid


class WantListEntryTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_init(self):
        cid = py_cid.make_cid('QmaozNR7DZHQK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdT3L4')
        e = WantListEntry(cid)
        self.assertEqual(e.cid, cid)
        self.assertEqual(e._ref_count, 1)
        self.assertEqual(e.priority, 1)
        e = WantListEntry(cid, 5)
        self.assertEqual(e.cid, cid)
        self.assertEqual(e._ref_count, 1)
        self.assertEqual(e.priority, 5)
        with self.assertRaises(ValueError):
            WantListEntry('df')

    def test_inc(self):
        cid = py_cid.make_cid('QmaozNR7DZHQK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdT3L4')
        e = WantListEntry(cid)
        self.assertEqual(e._ref_count, 1)
        e.inc_ref_count()
        self.assertEqual(e._ref_count, 2)

    def test_dec(self):
        cid = py_cid.make_cid('QmaozNR7DZHQK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdT3L4')
        e = WantListEntry(cid)
        self.assertEqual(e._ref_count, 1)
        e.dec_ref_count()
        self.assertEqual(e._ref_count, 0)
        e.dec_ref_count()
        self.assertEqual(e._ref_count, 0)

    def test_has_refs(self):
        cid = py_cid.make_cid('QmaozNR7DZHQK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdT3L4')
        e = WantListEntry(cid)
        self.assertTrue(e.has_refs())
        e.dec_ref_count()
        self.assertFalse(e.has_refs())
        e.dec_ref_count()
        self.assertFalse(e.has_refs())

    def test_str(self):
        cid = py_cid.make_cid('QmaozNR7DZHQK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdT3L4')
        e = WantListEntry(cid, 5)
        expected = f'WantListEntry(cid={str(cid)}, priority=5) refs:1'
        self.assertEqual(expected, str(e))

    def test_eq(self):
        cid = py_cid.make_cid('QmaozNR7DZHQK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdT3L4')
        e = WantListEntry(cid, 5)
        e2 = WantListEntry(cid, 5)
        self.assertTrue(e.equals(e2))
        self.assertTrue(e == e2)
        e2.inc_ref_count()
        self.assertFalse(e.equals(e2))  # different _ref_count
        self.assertFalse(e == e2)  # different _ref_count
        e2 = WantListEntry(cid, 3)
        self.assertFalse(e.equals(e2))  # different priority
        self.assertFalse(e == e2)  # different priority
        cid2 = py_cid.make_cid('QmaozNR7DZHQK1ZcU9p7QdrshMvXqW71ZcU9p7QdrshMpa')
        e2 = WantListEntry(cid2, 5)
        self.assertFalse(e.equals(e2))  # different cid
        self.assertFalse(e == e2)  # different cid


if __name__ == '__main__':
    unittest.main()
