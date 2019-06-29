import cid as py_cid
import pytest
from bitswap import MessageEntry
from bitswap import WantListEntry


def test_init_cid_priority():
    cid = py_cid.make_cid('QmaozNR7DZHQK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdT3L4')
    m = MessageEntry(cid, False)
    assert m.entry == WantListEntry(cid)
    assert m.cid == cid
    assert m.cancel == False
    assert m.priority == 1
    m = MessageEntry(cid, True, 5)
    assert m.entry == WantListEntry(cid, 5)
    assert m.cid == cid
    assert m.cancel == True
    assert m.priority == 5
    with pytest.raises(ValueError):
        MessageEntry('df', True)


def test_str():
    cid = py_cid.make_cid('QmaozNR7DZHQK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdT3L4')
    m = MessageEntry(cid, True, 5)
    expected = f'BitswapMessageEntry (cid={str(cid)}, priority=5, cancel=True)'
    assert expected == str(m)


def test_eq():
    cid = py_cid.make_cid('QmaozNR7DZHQK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdT3L4')
    m = MessageEntry(cid, True, 5)
    m2 = MessageEntry(cid, True, 5)
    assert m.equals(m2)
    assert m == m2
    m2.cancel = False
    assert not (m.equals(m2))  # different cancel
    assert not (m == m2)  # different cancel
    cid2 = py_cid.make_cid('QmaozNR7DZHQK1ZcU9p7QdrshMvXqW71ZcU9p7QdrshMpa')
    m2 = MessageEntry(cid2, True, 5)
    assert not (m.equals(m2))  # different cid
    assert not (m == m2)  # different cid
