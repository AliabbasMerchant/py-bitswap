import cid as py_cid
from typing import Union


class WantListEntry:
    def __init__(self, cid: Union[py_cid.CIDv0, py_cid.CIDv1], priority: int = 1):
        if not py_cid.is_cid(str(cid)):
            raise ValueError(f"{cid} is not a valid cid")
        self._ref_count: int = 1
        self.cid = cid
        self.priority = priority

    def inc_ref_count(self) -> None:
        self._ref_count += 1

    def dec_ref_count(self) -> None:
        minus_1 = self._ref_count - 1
        self._ref_count = 0 if 0 > minus_1 else minus_1

    def has_refs(self) -> bool:
        return self._ref_count > 0

    def __str__(self) -> str:
        return f'WantListEntry (cid={str(self.cid)}, priority={self.priority}) refs={self._ref_count}'

    def __eq__(self, other: 'WantListEntry') -> bool:
        return self._ref_count == other._ref_count and str(self.cid) == str(
            other.cid) and self.priority == other.priority
