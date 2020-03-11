import cid as py_cid
import libp2p
from bitswap.decision_engine import Ledger

peer_id = libp2p.peer.id.id_b58_decode("QmYyQSo1c1Ym7orWxLYvCrM2EmxFTANf8wXmmE7DWjhx5N")


def test_init():
    ledger = Ledger(peer_id)
    assert ledger.partner == peer_id
    assert len(ledger.wantlist) == 0
    assert ledger.exchange_count == 0
    assert ledger.last_exchange is None
    assert ledger.accounting['bytesSent'] == 0
    assert ledger.accounting['bytesReceived'] == 0


def test_sent_bytes():
    ledger = Ledger(peer_id)
    n1, n2 = 5, 17
    ledger.sent_bytes(n1)
    assert ledger.exchange_count == 1
    assert ledger.accounting['bytesSent'] == n1
    ledger.sent_bytes(n2)
    assert ledger.exchange_count == 2
    assert ledger.accounting['bytesSent'] == n1 + n2


def test_received_bytes():
    ledger = Ledger(peer_id)
    n1, n2 = 5, 17
    ledger.received_bytes(n1)
    assert ledger.exchange_count == 1
    assert ledger.accounting['bytesReceived'] == n1
    ledger.received_bytes(n2)
    assert ledger.exchange_count == 2
    assert ledger.accounting['bytesReceived'] == n1 + n2


def test_wants():
    ledger = Ledger(peer_id)
    cid = py_cid.make_cid('QmaozNR7DZHQK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdT3L4')
    ledger.wants(cid, 1)
    assert cid in ledger.wantlist


def test_cancel_want():
    ledger = Ledger(peer_id)
    cid = py_cid.make_cid('QmaozNR7DZHQK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdT3L4')
    ledger.wants(cid, 1)
    ledger.wants(cid, 1)
    ledger.cancel_want(cid)
    assert cid in ledger.wantlist
    ledger.cancel_want(cid)
    assert cid not in ledger.wantlist


def test_wantlist_contains():
    ledger = Ledger(peer_id)
    cid = py_cid.make_cid('QmaozNR7DZHQK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdT3L4')
    ledger.wants(cid, 1)
    assert ledger.wantlist_contains(cid)


def test_contains():
    ledger = Ledger(peer_id)
    cid = py_cid.make_cid('QmaozNR7DZHQK1ZcU9p7QdrshMvXqWK6gpu5rmrkPdT3L4')
    ledger.wants(cid, 1)
    assert cid in ledger


def test_debt_ratio():
    ledger = Ledger(peer_id)
    n1, n2 = 5, 17
    ledger.sent_bytes(n1)
    ledger.received_bytes(n2)
    assert ledger.debt_ratio() == n1 / (n2 + 1)
