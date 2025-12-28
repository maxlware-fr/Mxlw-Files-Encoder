import os
import base64
import getpass
from pathlib import Path
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet

# ===== Couleurs terminal =====
class C:
    HEADER = "\033[95m"
    OK = "\033[92m"
    WARN = "\033[93m"
    ERROR = "\033[91m"
    CYAN = "\033[96m"
    BLUE = "\033[94m"
    RESET = "\033[0m"
    BOLD = "\033[1m"


MAGIC_HEADER = b"MXLWv1"


def color(text, c):
    return f"{c}{text}{C.RESET}"


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


def encrypt_file(path: Path):
    if not path.exists() or not path.is_file():
        print(color("Fichier introuvable.", C.WARN))
        return

    print(color("\n→ Chiffrement du fichier…", C.CYAN))
    password = getpass.getpass(color("Mot de passe : ", C.BLUE))

    salt = os.urandom(16)
    key = derive_key(password, salt)
    cipher = Fernet(key)

    data = path.read_bytes()
    encrypted = cipher.encrypt(data)

    payload = MAGIC_HEADER + salt + encrypted
    out_path = path.with_suffix(path.suffix + ".mxlw")
    out_path.write_bytes(payload)

    print(color(f"✔ Fichier chiffré → {out_path}", C.OK))


def decrypt_file(path: Path):
    if not path.exists():
        print(color("Fichier introuvable.", C.WARN))
        return

    data = path.read_bytes()

    if not data.startswith(MAGIC_HEADER):
        print(color("Ce fichier n'est pas un format .mxlw valide.", C.ERROR))
        return

    print(color("\n→ Déchiffrement du fichier…", C.CYAN))

    salt = data[len(MAGIC_HEADER):len(MAGIC_HEADER)+16]
    encrypted = data[len(MAGIC_HEADER)+16:]

    password = getpass.getpass(color("Mot de passe : ", C.BLUE))
    key = derive_key(password, salt)
    cipher = Fernet(key)

    try:
            decrypted = cipher.decrypt(encrypted)
    except Exception:
            print(color("Mot de passe incorrect ou fichier altéré.", C.ERROR))
            return

    out_path = path.with_suffix(".decrypted")
    out_path.write_bytes(decrypted)

    print(color(f"✔ Fichier déchiffré → {out_path}", C.OK))


def main():
    while True:
        print("\n" + color("=== MXLW Secure Encoder ===", C.BOLD))
        print(color("1) Chiffrer un fichier", C.CYAN))
        print(color("2) Déchiffrer un fichier .mxlw", C.CYAN))
        print(color("3) Quitter", C.CYAN))

        choice = input(color("\nChoix → ", C.BLUE)).strip()

        if choice == "1":
            filepath = input(color("Chemin du fichier : ", C.BLUE)).strip()
            encrypt_file(Path(filepath))

        elif choice == "2":
            filepath = input(color("Chemin du fichier .mxlw : ", C.BLUE)).strip()
            decrypt_file(Path(filepath))

        elif choice == "3":
            print(color("Sortie du programme.", C.HEADER))
            break

        else:
            print(color("Commande inconnue.", C.WARN))


if __name__ == "__main__":
    main()
