import libp2p
import time
import cid as py_cid
from typing import Union, Optional

from bitswap.wantlist import WantList


class Ledger:
    def __init__(self, peer_id: 'libp2p.peer.id.ID'):
        self.partner = peer_id
        self.wantlist = WantList()
        self.exchange_count = 0
        self.last_exchange = None
        self.accounting = {
            'bytesSent': 0,
            'bytesReceived': 0
        }
        # self.sent_to_peer = {}

    def sent_bytes(self, n: int) -> None:
        self.exchange_count += 1
        self.last_exchange = time.time()
        self.accounting['bytesSent'] += n

    def received_bytes(self, n: int) -> None:
        self.exchange_count += 1
        self.last_exchange = time.time()
        self.accounting['bytesReceived'] += n

    def wants(self, cid: Union[py_cid.CIDv0, py_cid.CIDv1], priority: Optional[int] = 1) -> None:
        self.wantlist.add(cid, priority)

    def cancel_want(self, cid: Union[py_cid.CIDv0, py_cid.CIDv1]) -> None:
        self.wantlist.remove(cid)

    def wantlist_contains(self, cid: Union[py_cid.CIDv0, py_cid.CIDv1]) -> bool:
        return cid in self.wantlist

    def __contains__(self, cid: Union[py_cid.CIDv0, py_cid.CIDv1]) -> bool:
        return cid in self.wantlist

    def debt_ratio(self) -> float:
        return self.accounting['bytesSent'] / (self.accounting['bytesReceived'] + 1)
