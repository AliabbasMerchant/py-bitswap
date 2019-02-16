from bitswap import WantList
import unittest
import cid as py_cid


class WantListTest(unittest.TestCase):

    def setUp(self):
        self.wl = WantList()
        print('set up')

    def test_add(self):
        cid = py_cid.make_cid('QmaozNR7DZHQK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdT3L4')

        self.assertEqual('a' * 4, 'aaaa')

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_strip(self):
        s = 'geeksforgeeks'
        self.assertEqual(s.strip('geek'), 'sforgeeks')

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
