from bitswap import WantList
import unittest
import cid as py_cid


class WantListTest(unittest.TestCase):

    def setUp(self):  # test_init
        self.wl = WantList()

    def test_add(self):
        cid = py_cid.make_cid('QmaozNR7DZHQK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdT3L4')
        self.wl.add(cid)
        self.assertTrue(str(cid) in self.wl.entries)
        self.assertEqual(1, self.wl.entries[str(cid)].priority)
        self.wl.add(cid, 3)
        self.assertTrue(str(cid) in self.wl.entries)
        self.assertEqual(3, self.wl.entries[str(cid)].priority)
        self.assertEqual(2, self.wl.entries[str(cid)]._ref_count)

    def test_remove(self):
        cid = py_cid.make_cid('QmaozNR7DZHQK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdT3L4')
        self.wl.remove(cid)
        self.assertFalse(str(cid) in self.wl.entries)
        self.wl.add(cid)
        self.wl.remove(cid)
        self.assertFalse(str(cid) in self.wl.entries)
        self.wl.add(cid)
        self.wl.add(cid)
        self.wl.add(cid)
        self.wl.remove(cid)
        self.assertTrue(str(cid) in self.wl.entries)
        self.assertEqual(2, self.wl.entries[str(cid)]._ref_count)
        self.wl.remove(cid)
        self.assertTrue(str(cid) in self.wl.entries)
        self.assertEqual(1, self.wl.entries[str(cid)]._ref_count)
        self.wl.remove(cid)
        self.assertFalse(str(cid) in self.wl.entries)

    def test_force_remove(self):
        cid = py_cid.make_cid('QmaozNR7DZHQK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdT3L4')
        self.wl.add(cid)
        self.wl.add(cid)
        self.wl.force_remove(cid)
        self.assertFalse(str(cid) in self.wl.entries)

    def test_sorted_entries(self):
        with self.assertRaises(NotImplementedError):
            self.wl.sorted_entries()

    def test_len(self):
        cid = py_cid.make_cid('QmaozNR7DZHQK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdT3L4')
        self.assertEqual(0, len(self.wl))
        self.wl.add(cid)
        self.wl.add(cid)
        self.assertEqual(1, len(self.wl))
        self.wl.add(py_cid.make_cid('QmaozNR7DZddK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdTPdT'))
        self.assertEqual(2, len(self.wl))

    def test_str(self):
        self.wl.add(py_cid.make_cid('QmaozNR7DZHQK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdT3L4'))
        self.wl.add(py_cid.make_cid('QmaozNR7DZddK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdTPdT'))
        expected = 'WantList, number_of_entries=2'
        self.assertEqual(expected, str(self.wl))

    def test_iter(self):
        cids = [py_cid.make_cid('QmaozNR7DZHQK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdT3L4'),
                py_cid.make_cid('QmaozNR7DZddK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdTPdT')]
        self.wl.add(cids[0])
        self.wl.add(cids[1])
        count = 0
        for i in self.wl:
            self.assertEqual(str(cids[count]), i)
            count += 1

    def test_contains(self):
        cids = [py_cid.make_cid('QmaozNR7DZHQK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdT3L4'),
                py_cid.make_cid('QmaozNR7DZddK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdTPdT')]
        self.wl.add(cids[0])
        self.assertTrue(cids[0] in self.wl)
        self.assertFalse(cids[1] in self.wl)
        self.wl.add(cids[1])
        self.assertTrue(cids[1] in self.wl)


if __name__ == '__main__':
    unittest.main()
