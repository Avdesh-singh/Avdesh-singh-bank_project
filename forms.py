import hashlib
def hash_value(a):
    return hashlib.sha256(str(a).encode()).hexdigest()
