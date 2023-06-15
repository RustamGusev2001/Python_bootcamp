from gaining_access import Key


def createKey():
    key = Key()
    print(key.passphrase)
    print(key.__str__())
    print(key.__len__())
    print(key > 9000)
    print(key[404])
    return key


def test_pass(key):
    assert key.passphrase == "zax2rulez", 'key.passphrase == "zax2rulez"'
    print('Test pass Ok')


def test_str(key):
    assert str(key) == "GeneralTsoKeycard", 'str(key) == "GeneralTsoKeycard"'
    print('Test str Ok')

def test_len(key):
    assert len(key) == 1337, 'len(key) == 1337'
    print('Test len Ok')


def test_gt(key):
    assert key > 9000, 'key > 9000'
    print('Test gt Ok')



def test_getitem(key):
    assert key[404] == 3, 'key[404] == 3'
    print('Test getitem Ok')


if __name__ == "__main__":
    key = createKey()
    test_pass(key)
    test_str(key)
    test_len(key)
    test_gt(key)
    test_getitem(key)