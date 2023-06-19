import hashlib
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

# Геш-значення, для якого потрібно знайти прообраз
hash_value = "d182aed568b01fee105557a1d173791c798030db267cf94e17102b94dcbbda3c"

# Функція, яка знаходить прообраз геш-функції за допомогою бібліотеки hashlib
def find_preimage_hashlib(hash_value, length):
    for i in range(100000000):
        data = str(i).encode('utf-8')
        hash_object = hashlib.sha256(data)
        if hash_object.hexdigest()[:length] == hash_value:
            return data
    return None

# Функція, яка знаходить прообраз геш-функції за допомогою бібліотеки cryptography
def find_preimage_cryptography(hash_value, length):
    for i in range(100000000):
        data = str(i).encode('utf-8')
        digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
        digest.update(data)
        hash_object = digest.finalize()
        if hash_object.hex()[:length] == hash_value:
            return data
    return None


# Знаходимо прообраз геш-функції за допомогою різних бібліотек
preimage_hashlib = find_preimage_hashlib(hash_value, 64)
preimage_cryptography = find_preimage_cryptography(hash_value, 64)

# Виводимо результат
if preimage_hashlib is not None:
    print("Прообраз геш-функції, знайдений за допомогою бібліотеки hashlib:", preimage_hashlib)
if preimage_cryptography is not None:
    print("Прообраз геш-функції, знайдений за допомогою бібліотеки cryptography:", preimage_cryptography)
