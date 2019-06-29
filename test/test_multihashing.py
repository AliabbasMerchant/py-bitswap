import multihash
from Crypto.Hash import SHA1
from bitswap import multihashing


functions = {
    'sha1': SHA1
}
data = b"HelloMultihashing@%4&^&6543"


def test_create_hash():
    for func in functions:
        h1 = multihashing.create_hash(func)
        h2 = functions[func].new()
        assert str(h1)[:str(h1).rindex("at")] == str(h2)[:str(h2).rindex("at")]


def test_digest():
    encoded = multihashing.digest(data, 'sha1', 12)
    assert len(encoded) == 12


def test_multihashing():
    for func in functions:
        h = functions[func].new()
        h.update(data)
        d = h.digest()
        ideal = multihash.encode(d, func)
        got = multihashing.multihashing(data, func)
        assert ideal == got
        ideal = multihash.encode(d[:10], func, 10)
        got = multihashing.multihashing(data, func, 10)
        assert ideal == got


def test_verify():
    for func in functions:
        h = functions[func].new()
        h.update(data)
        d = h.digest()
        ideal = multihash.encode(d, func)
        assert multihashing.verify(ideal, data)


def test_validity():
    expected = {
        'sha1': "11 14 22 67 fb 69 f1 e1 7f 15 58 83 c2 fa df 22 71 95 7d df 96 62".replace(" ", ""),
        'sha2-256':
            "12 20 91 3d b4 c7 62 ba 95 d7 6c a2 55 9d 04 9d 2c 84 54 a0 11 a6 a4 b8 58 5c 12 ba 74 b5 b8 e9 b1 ab".
                replace(" ", ""),
    }
    for func in expected:
        assert expected[func] == multihashing.multihashing(data, func).hex()
