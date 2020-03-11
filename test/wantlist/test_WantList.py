import cid as py_cid
from bitswap import WantList


def test_init():
    wl = WantList()
    assert len(wl.entries.keys()) == 0


def test_add():
    wl = WantList()
    cid = py_cid.make_cid('QmaozNR7DZHQK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdT3L4')
    wl.add(cid)
    assert str(cid) in wl.entries
    assert 1 == wl.entries[str(cid)].priority
    wl.add(cid, 3)
    assert str(cid) in wl.entries
    assert 3 == wl.entries[str(cid)].priority
    assert 2 == wl.entries[str(cid)]._ref_count


def test_remove():
    wl = WantList()
    cid = py_cid.make_cid('QmaozNR7DZHQK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdT3L4')
    wl.remove(cid)
    assert not (str(cid) in wl.entries)
    wl.add(cid)
    wl.remove(cid)
    assert not (str(cid) in wl.entries)
    wl.add(cid)
    wl.add(cid)
    wl.add(cid)
    wl.remove(cid)
    assert str(cid) in wl.entries
    assert 2 == wl.entries[str(cid)]._ref_count
    wl.remove(cid)
    assert str(cid) in wl.entries
    assert 1 == wl.entries[str(cid)]._ref_count
    wl.remove(cid)
    assert not (str(cid) in wl.entries)


def test_force_remove():
    wl = WantList()
    cid = py_cid.make_cid('QmaozNR7DZHQK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdT3L4')
    wl.add(cid)
    wl.add(cid)
    wl.force_remove(cid)
    assert not (str(cid) in wl.entries)


def test_sorted_entries():
    wl = WantList()
    wl.add(py_cid.make_cid('QmaozNR7DZHQK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdT3L4'))
    # TODO add some more cids
    sorted_entries = wl.sorted_entries()
    c = None
    for index, entry in enumerate(sorted_entries.keys()):
        if index == 0:
            c = entry
        else:
            assert entry >= c
            c = entry


def test_len():
    wl = WantList()
    cid = py_cid.make_cid('QmaozNR7DZHQK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdT3L4')
    assert 0 == len(wl)
    wl.add(cid)
    wl.add(cid)
    assert 1 == len(wl)
    wl.add(py_cid.make_cid('QmaozNR7DZddK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdTPdT'))
    assert 2 == len(wl)


def test_str():
    wl = WantList()
    wl.add(py_cid.make_cid('QmaozNR7DZHQK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdT3L4'))
    wl.add(py_cid.make_cid('QmaozNR7DZddK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdTPdT'))
    expected = 'WantList, number_of_entries=2'
    assert expected == str(wl)


def test_iter():
    wl = WantList()
    cids = [py_cid.make_cid('QmaozNR7DZHQK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdT3L4'),
            py_cid.make_cid('QmaozNR7DZddK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdTPdT')]
    wl.add(cids[0])
    wl.add(cids[1])
    assert len(wl) == 2
    for i in wl:
        assert i in [str(cid) for cid in cids]


def test_contains():
    wl = WantList()
    cids = [py_cid.make_cid('QmaozNR7DZHQK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdT3L4'),
            py_cid.make_cid('QmaozNR7DZddK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdTPdT')]
    wl.add(cids[0])
    assert cids[0] in wl
    assert not (cids[1] in wl)
    wl.add(cids[1])
    assert cids[1] in wl
