import pytest
import cid as py_cid
from bitswap.wantlist import WantListEntry


def test_init():
    cid = py_cid.make_cid('QmaozNR7DZHQK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdT3L4')
    e = WantListEntry(cid)
    assert e.cid == cid
    assert e._ref_count == 1
    assert e.priority == 1
    e = WantListEntry(cid, 5)
    assert e.cid == cid
    assert e._ref_count == 1
    assert e.priority == 5
    with pytest.raises(ValueError):
        WantListEntry('df')


def test_inc():
    cid = py_cid.make_cid('QmaozNR7DZHQK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdT3L4')
    e = WantListEntry(cid)
    assert e._ref_count == 1
    e.inc_ref_count()
    assert e._ref_count == 2


def test_dec():
    cid = py_cid.make_cid('QmaozNR7DZHQK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdT3L4')
    e = WantListEntry(cid)
    assert e._ref_count == 1
    e.dec_ref_count()
    assert e._ref_count == 0
    e.dec_ref_count()
    assert e._ref_count == 0


def test_has_refs():
    cid = py_cid.make_cid('QmaozNR7DZHQK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdT3L4')
    e = WantListEntry(cid)
    assert e.has_refs()
    e.dec_ref_count()
    assert not (e.has_refs())
    e.dec_ref_count()
    assert not (e.has_refs())


def test_str():
    cid = py_cid.make_cid('QmaozNR7DZHQK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdT3L4')
    e = WantListEntry(cid, 5)
    expected = f'WantListEntry (cid={str(cid)}, priority=5) refs=1'
    assert expected, str(e)


def test_eq():
    cid = py_cid.make_cid('QmaozNR7DZHQK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdT3L4')
    e = WantListEntry(cid, 5)
    e2 = WantListEntry(cid, 5)
    assert e == e2
    e2.inc_ref_count()
    assert not (e == e2)  # different _ref_count
    e2 = WantListEntry(cid, 3)
    assert not (e == e2)  # different priority
    cid2 = py_cid.make_cid('QmaozNR7DZHQK1ZcU9p7QdrshMvXqW71ZcU9p7QdrshMpa')
    e2 = WantListEntry(cid2, 5)
    assert not (e == e2)  # different cid
