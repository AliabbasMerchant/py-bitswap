import logging
import typing
import libp2p


def logger(peer_id: typing.Optional['libp2p.peer.id.ID'] = None, subsystem: typing.Optional[str] = None) -> logging:
    name = ['bitswap']
    if subsystem:
        name.append(subsystem)
    if peer_id:
        name.append(f"{peer_id.pretty()}")
    # TODO: Change the level later on
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s:%(message)s',
                        datefmt='%m/%d-%H:%M:%S')
    _logger = logging.getLogger(':'.join(name))
    return _logger
