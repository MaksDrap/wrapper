import hashlib
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

# Геш-значення, для якого потрібно знайти прообраз
hash_value = "d182aed568b01fee105557a1d173791c798030db267cf94e17102b94dcbbda3c"

# Функція, яка знаходить прообраз геш-функції
def find_preimage(hash_value, length):
    for i in range(10050000):
        data = str(i).encode('utf-8')
        hash_object = hashes.Hash(hashes.SHA256(), backend=default_backend())
        hash_object.update(data)
        if hash_object.finalize().hex()[:length] == hash_value:
            return data
    return None

# Знаходимо прообраз геш-функції
preimage = find_preimage(hash_value, 64)

# Виводимо результат
if preimage is None:
    print("Прообраз не знайдено")
else:
    print("Прообраз геш-функції:", preimage)