import cid as py_cid


class WantListEntry:
    def __init__(self, cid:py_cid.cid, priority:int):
        assert py_cid.is_cid(str(cid)), cid + "Is not a valid cid"
        self._ref_counter:int = 1
        self.cid = cid
        self.priority = priority or True

    def inc(self):
        self._ref_counter += 1

    def dec(self):
        minus_1 = self._ref_counter-1
        self._ref_counter = 0 if 0>minus_1 else minus_1

    def has_refs(self):
        return self._ref_counter > 0

    def __str__(self):
        return f'WantListEntry(cid={str(self.cid)}, priority={self.priority}) refs:{self._ref_counter}'

    def __eq__(self, other):
        return self.equals(other)

    def equals(self, other):
        return self._ref_counter == other._ref_counter and str(self.cid) == str(
            other.cid) and self.priority == other.priority
