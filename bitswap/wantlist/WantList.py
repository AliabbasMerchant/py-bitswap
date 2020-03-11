from .WantListEntry import WantListEntry
import cid as py_cid
from typing import Union, Optional


class WantList:

    def __init__(self):
        self.entries: dict = {}
        # self._stats = stats

    def add(self, cid: Union[py_cid.CIDv0, py_cid.CIDv1], priority: Optional[int] = 1) -> None:
        cid_str = str(cid)
        entry = self.entries.get(cid_str)
        if entry is not None:
            entry.inc_ref_count()
            entry.priority = priority  # TODO: Why ? Shouldn't we store the max of the priorities?
        else:
            self.entries[cid_str] = WantListEntry(cid, priority)
            # if self._stats is not None:
            #     self._stats.push(None, 'WantListSize', 1)

    def remove(self, cid: Union[py_cid.CIDv0, py_cid.CIDv1]) -> None:
        cid_str = str(cid)
        entry = self.entries.get(cid_str)
        if entry is not None:
            entry.dec_ref_count()
            if not entry.has_refs():  # don't delete if it has refs
                del self.entries[cid_str]
                # if self._stats is not None:
                #     self._stats.push(None, 'WantListSize', -1)

    def force_remove(self, cid: Union[py_cid.CIDv0, py_cid.CIDv1]) -> None:
        cid_str = str(cid)
        if self.entries.get(cid_str) is not None:
            del self.entries[cid_str]

    def sorted_entries(self):
        # sorted by value
        return {k: v for k, v in sorted(self.entries.items(), key=lambda item: item[1])}

    def __len__(self) -> int:
        return len(self.entries)

    def __str__(self) -> str:
        return f'WantList, number_of_entries={len(self.entries)}'

    def __iter__(self):
        yield from self.entries

    def __contains__(self, item: Union[py_cid.CIDv0, py_cid.CIDv1]) -> bool:
        return str(item) in self.entries
