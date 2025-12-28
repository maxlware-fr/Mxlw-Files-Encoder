from pathlib import Path
from .crypto import encrypt_bytes, decrypt_bytes


def encrypt_file(path: Path, password: str) -> Path:
    data = path.read_bytes()
    encrypted = encrypt_bytes(data, password)

    out_path = path.with_suffix(path.suffix + ".mxlw")
    out_path.write_bytes(encrypted)
    return out_path


def decrypt_file(path: Path, password: str) -> Path:
    payload = path.read_bytes()
    decrypted = decrypt_bytes(payload, password)

    out_path = path.with_suffix(".decrypted")
    out_path.write_bytes(decrypted)
    return out_path
