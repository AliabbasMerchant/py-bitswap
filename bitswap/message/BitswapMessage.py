from .message_pb2 import Message
import cid as py_cid
import varint
from .MessageEntry import MessageEntry
from bitswap import Block
from typing import Union

'''
const isEqualWith = require('lodash.isequalwith')
const each = require('async/each')
const nextTick = require('async/nextTick')
const codecName = require('multicodec/src/name-table')
const multihashing = require('multihashing-async')
const pbm = protons(require('./message.proto'))
'''


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

    def serialize_to_bitswap_110(self):
        """
        Serializes to Bitswap Message protobuf of version 1.1.0
        """
        # TODO
        raise NotImplementedError()

    def __eq__(self, other: 'BitswapMessage'):
        return self.full == other.full and \
               self.want_list == other.want_list and \
               self.blocks == other.blocks

    def equals(self, other: 'BitswapMessage'):
        return self == other

    def __str__(self):
        return f'BitswapMessage (full={self.full}) , want_list={self.want_list.keys()}, blocks={self.blocks.keys()}'

    @staticmethod
    def deserialize(raw):
        # TODO
        raise NotImplementedError()
