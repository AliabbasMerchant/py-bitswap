from bitswap.wantlist import WantListEntry
import cid as py_cid
from typing import Union


class MessageEntry:
    def __init__(self, cid: Union[py_cid.CIDv0, py_cid.CIDv1], cancel: bool, priority: int = 1):
        if not py_cid.is_cid(str(cid)):
            raise ValueError(f"{cid} is not a valid cid")
        self.entry = WantListEntry(cid, priority)
        self.cancel = bool(cancel)

    @property
    def cid(self) -> Union[py_cid.CIDv0, py_cid.CIDv1]:
        return self.entry.cid

    @cid.setter
    def cid(self, cid) -> None:
        self.entry.cid = cid

    @property
    def priority(self) -> int:
        return self.entry.priority

    @priority.setter
    def priority(self, priority) -> None:
        self.entry.priority = priority

    def __str__(self) -> str:
        return f'BitswapMessageEntry (cid={str(self.cid)}, priority={self.priority}, cancel={self.cancel})'

    def __eq__(self, other: 'MessageEntry') -> bool:
        return self.cancel == other.cancel and self.entry == other.entry
