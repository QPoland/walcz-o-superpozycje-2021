from hashlib import sha512

def _counts_to_str(counts: dict):
    return str(sorted(list(zip(counts.keys(), counts.values()))))

def _get_hash(counts: dict):
    return sha512(str.encode(_counts_to_str(counts))).hexdigest()