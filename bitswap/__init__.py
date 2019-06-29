"""Python implementation of the Bitswap 'data exchange' protocol used by IPFS"""

__version__ = '0.0.1'

from .IPFSBlock import Block
from .wantlist import WantListEntry, WantList
from .message import MessageEntry, BitswapMessage
