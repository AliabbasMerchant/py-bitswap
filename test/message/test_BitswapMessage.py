import pytest
import cid as py_cid
from bitswap import BitswapMessage


def test_empty():
    pass


def test_add_entry():
    bm = BitswapMessage(False)
    cid = py_cid.make_cid('QmaozNR7DZHQK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdT3L4')
    cid_str = str(cid)
    with pytest.raises(ValueError):
        bm.add_entry('df', True)


def test_add_block():
    pass


def test_cancel():
    pass


def test_equals():
    pass


def test_serialize_to_bitswap_100():
    pass


def test_serialize_to_bitswap_110():
    pass


def test_deserialize():
    pass


def test_str():
    pass
