from bitswap import WantListEntry
import cid as py_cid


class MessageEntry:
    def __init__(self, cid: py_cid.cid, cancel: bool, priority: int = 1):
        if not py_cid.is_cid(str(cid)):
            raise ValueError(f"{cid} is not a valid cid")
        self.entry = WantListEntry(cid, priority)
        self.cancel = bool(cancel)

    @property
    def cid(self):
        return self.entry.cid

    @cid.setter
    def cid(self, cid):
        self.entry.cid = cid

    @property
    def priority(self):
        return self.entry.priority

    @priority.setter
    def priority(self, priority):
        self.entry.priority = priority

    def __str__(self):
        return f'BitswapMessageEntry (cid={str(self.cid)}, priority={self.priority}, cancel={self.cancel})'

    def __eq__(self, other: 'MessageEntry'):
        return self.cancel == other.cancel and \
               self.entry == other.entry

    def equals(self, other: 'MessageEntry'):
        return self == other
