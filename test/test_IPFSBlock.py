import pytest
import cid as py_cid
from bitswap import Block

cid = py_cid.make_cid('QmaozNR7DZHQK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdT3L4')
data = bytes("SomeData", "utf-8")
block = Block(data, cid)


def test_getters():
    assert block.data == data
    assert block.cid == cid


def test_setters():
    with pytest.raises(AttributeError):
        block.data = "SomeData"
    with pytest.raises(AttributeError):
        block.cid = "CID"
