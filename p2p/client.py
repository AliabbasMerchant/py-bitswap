import asyncio
import sys

import multiaddr

from libp2p import new_node
from libp2p.peer.peerinfo import info_from_p2p_addr


async def read_data(stream):
    while True:
        read_string = await stream.read()
        if read_string is not None:
            read_string = read_string.decode()
            if read_string != "\n":
                # Green console colour: 	\x1b[32m
                # Reset console colour: 	\x1b[0m
                print("\n\x1b[32m %s\x1b[0m " % read_string, end="")


async def write_data(stream):
    loop = asyncio.get_event_loop()
    while True:
        line = await loop.run_in_executor(None, sys.stdin.readline)
        await stream.write(line.encode())


async def run(port, destination):
    host = await new_node(transport_opt=["/ip4/127.0.0.1/tcp/%s" % port])
    m = multiaddr.Multiaddr(destination)
    info = info_from_p2p_addr(m)
    # Associate the peer with local ip address
    await host.connect(info)

    # Start a stream with the destination.
    # Multiaddress of the destination peer is fetched from the peerstore using 'peerId'.
    stream = await host.new_stream(info.peer_id, [PROTOCOL_ID])

    asyncio.ensure_future(read_data(stream))
    asyncio.ensure_future(write_data(stream))
    print("Connected to peer %s" % info.addrs[0])


def main(port, destination):
    loop = asyncio.get_event_loop()
    try:
        asyncio.ensure_future(run(port, destination))
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()


if __name__ == '__main__':
    PROTOCOL_ID = '/chat/1.0.0'
    port = 9000
    destination = '/ip4/127.0.0.1/tcp/9001/p2p/QmaeUF2b2TQcsu3rTiyygPnULGh3wQnDxi5AKDyEKKxSJx'
    main(port, destination)
