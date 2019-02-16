from .WantListEntry import WantListEntry
from collections import OrderedDict
import cid as py_cid


# TODO: stats
class WantList:
    # Entry = WantListEntry  # TODO: Why ?

    def __init__(self):
        self.entries = OrderedDict()
        # self._stats = stats

    def add(self, cid: py_cid.cid, priority: int = 1):
        cid_str = str(cid)
        entry = self.entries.get(cid_str)
        if entry is not None:
            entry.inc_ref_count()
            entry.priority = priority  # TODO: Why ?
        else:
            self.entries[cid_str] = WantListEntry(cid, priority)
            # if self._stats is not None:
            #     self._stats.push(None, 'WantListSize', 1)

    def remove(self, cid: py_cid.cid):
        cid_str = str(cid)
        entry = self.entries.get(cid_str)
        if entry is not None:
            entry.dec_ref_count()
            if entry.has_refs():  # don't delete if it has refs
                return
            else:
                del self.entries[cid_str]
                # if self._stats is not None:
                #     self._stats.push(None, 'WantListSize', -1)

    def force_remove(self, cid: py_cid.cid):
        cid_str = str(cid)
        if self.entries.get(cid_str) is not None:
            del self.entries[cid_str]

    def sorted_entries(self):
        # TODO
        raise NotImplementedError()

    def __len__(self):
        return len(self.entries)

    def __str__(self):
        return f'WantList, number_of_entries={len(self.entries)}'

    def __iter__(self):
        yield from self.entries

    def __contains__(self, item: py_cid.cid):
        return str(item) in self.entries
