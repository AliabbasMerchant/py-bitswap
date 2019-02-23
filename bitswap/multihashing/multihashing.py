import multihash
from Crypto.Hash import SHA1, SHA256, SHA512

supported_functions = {
    0x11: SHA1,
    0x12: SHA256,
    0x13: SHA512
}


def digest(buffer, function, length=None):
    if not isinstance(buffer, bytes):
        raise TypeError('buffer must be a bytes object, not {}'.format(type(buffer)))
    h = create_hash(function)
    h.update(buffer)
    d = h.digest()
    if length:
        d = d[:length]
    return d


def create_hash(function):
    func = multihash.coerce_code(function)
    if func not in supported_functions:
        raise NotImplementedError('multihash function ' + function + ' not yet supported')
    return supported_functions[func].new()


def multihashing(buffer, function, length=None):
    if not isinstance(buffer, bytes):
        raise TypeError('buffer must be a bytes object, not {}'.format(type(buffer)))
    return multihash.encode(digest(buffer, function, length), function, length)


def verify(mh, buffer):
    if not isinstance(buffer, bytes):
        raise TypeError('buffer must be a bytes object, not {}'.format(type(buffer)))
    decoded = multihash.decode(mh)
    encoded = multihashing(buffer, decoded.name, decoded.length)
    return encoded == mh


__all__ = ['multihash', 'digest', 'create_hash', 'verify', 'multihashing', 'supported_functions']
