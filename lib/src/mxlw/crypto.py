import os
import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet

MAGIC_HEADER = b"MXLWv1"


def derive_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=200_000,
        backend=default_backend(),
    )
    key = kdf.derive(password.encode("utf-8"))
    return base64.urlsafe_b64encode(key)


def encrypt_bytes(data: bytes, password: str) -> bytes:
    salt = os.urandom(16)
    key = derive_key(password, salt)
    cipher = Fernet(key)
    encrypted = cipher.encrypt(data)
    return MAGIC_HEADER + salt + encrypted


def decrypt_bytes(payload: bytes, password: str) -> bytes:
    if not payload.startswith(MAGIC_HEADER):
        raise ValueError("Format MXLW invalide")

    salt = payload[len(MAGIC_HEADER):len(MAGIC_HEADER)+16]
    encrypted = payload[len(MAGIC_HEADER)+16:]

    key = derive_key(password, salt)
    cipher = Fernet(key)
    return cipher.decrypt(encrypted)
