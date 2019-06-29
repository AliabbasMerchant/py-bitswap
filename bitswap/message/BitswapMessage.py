from .message_pb2 import Message
import cid as py_cid
from .MessageEntry import MessageEntry
from typing import Union
from multicodec import get_prefix as mc_prefix
from multicodec.constants import CODE_TABLE
from multihash import get_prefix as mh_prefix

from bitswap import Block
from bitswap.multihashing import multihashing
from bitswap.varint_decoder import varint_decoder


def get_prefix(cid: Union[py_cid.CIDv0, py_cid.CIDv1]):
    return bytes(("0" + str(cid.version)).encode("utf-8").hex()) + bytes(mc_prefix(cid.codec)) + mh_prefix(
        cid.multihash)


class BitswapMessage:
    # Entry = MessageEntry  # TODO: Why ?
    def __init__(self, full: bool):
        self.full = full
        self.want_list = {}
        self.blocks = {}

    @property
    def empty(self):
        return len(self.blocks) == 0 and len(self.want_list) == 0

    def add_entry(self, cid: Union[py_cid.CIDv0, py_cid.CIDv1], cancel: bool, priority: int = 1):
        cid_str = str(cid)
        if not py_cid.is_cid(cid_str):
            raise ValueError(f"{cid} is not a valid cid")
        entry = self.want_list.get(cid_str)
        if entry is not None:
            entry.priority = priority  # TODO: why
            entry.cancel = cancel  # TODO: why
        else:
            self.want_list[cid_str] = MessageEntry(cid, cancel, priority)

    def add_block(self, block: Block):
        if not isinstance(block, Block):
            raise ValueError(f"{block} is not an IPFS block")
        self.blocks[str(block.cid)] = block

    def cancel(self, cid: Union[py_cid.CIDv0, py_cid.CIDv1]):
        cid_str = str(cid)
        if not py_cid.is_cid(cid_str):
            raise ValueError(f"{cid} is not a valid cid")
        del self.want_list[cid_str]
        self.add_entry(cid, cancel=True, priority=0)

    def serialize_to_bitswap_100(self):
        """
        Serializes to Bitswap Message protobuf of version 1.0.0
        """
        message = Message()
        wantlist = message.wantlist
        blocks = message.blocks
        # payload = message.payload

        entries = wantlist.entries
        wantlist.full = self.full
        for entry in self.want_list.values():
            msg = entries.add()
            msg.block = entry.cid.buffer
            msg.priority = int(entry.priority)
            msg.cancel = bool(entry.cancel)

        for b in self.blocks:
            block = blocks.add()
            # block.prefix =  TODO: empty?
            block.data = b.data

        return message.SerializeToString()

    def serialize_to_bitswap_110(self):
        """
        Serializes to Bitswap Message protobuf of version 1.1.0
        """
        message = Message()
        wantlist = message.wantlist
        # blocks = message.blocks
        payload = message.payload

        entries = wantlist.entries
        wantlist.full = self.full
        for entry in self.want_list.values():
            msg = entries.add()
            msg.block = entry.cid.buffer
            msg.priority = int(entry.priority)
            msg.cancel = bool(entry.cancel)

        for block in self.blocks:
            load = payload.add()
            load.prefix = get_prefix(block.cid)
            load.data = block.data

        return message.SerializeToString()

    def __eq__(self, other: 'BitswapMessage'):
        return self.full == other.full and self.want_list == other.want_list and self.blocks == other.blocks

    def equals(self, other: 'BitswapMessage'):
        return self == other

    def __str__(self):
        return f'BitswapMessage (full={self.full}) , want_list={self.want_list.keys()}, blocks={self.blocks.keys()}'

    @staticmethod
    def deserialize(raw):
        message = Message
        decoded = message.ParseFromString(raw)
        is_full = (decoded.wantlist and decoded.wantlist.full) or False
        bitswap_message = BitswapMessage(is_full)
        if decoded.wantlist:
            for entry in decoded.wantlist.entries:
                cid = py_cid.make_cid(entry.block)
                bitswap_message.add_entry(cid, entry.priority, entry.cancel)
        # Bitswap 1.0.0
        if len(decoded.blocks) > 0:
            for block in decoded.blocks:
                bitswap_message.add_block(Block(block, py_cid.make_cid(multihashing(block, 'sha2-256'))))
        # Bitswap 1.1.0
        if len(decoded.payload) > 0:
            for payload in decoded.payload:
                values = varint_decoder(payload.prefix)
                cid_version = values[0]
                multicodec = values[1]
                hash_algo = values[2]
                # hash_len = values[3]  # not needed, as yet
                hashed = multihashing(payload.data, hash_algo)
                cid = py_cid.make_cid(cid_version, CODE_TABLE[multicodec], hashed)
                bitswap_message.add_block(Block(payload.data, cid))
        return bitswap_message
